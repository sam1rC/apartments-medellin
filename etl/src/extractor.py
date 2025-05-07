from bs4 import BeautifulSoup
import requests
import json
import asyncio
from apt_parser import getAptInfo
from playwright.async_api import async_playwright
import time
import pandas as pd
import config

async def scrapeApartments(base_url,max_pages):

    apartmentsDf = pd.DataFrame(columns=config.APARTMENTS_DF_COLUMNS)

    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)  # Set to True for headless mode
        context = await browser.new_context()

        try:
            # Open initial page
            page = await context.new_page()
            await page.goto(base_url)
            await page.wait_for_load_state("networkidle")

            for current_page in range(1, max_pages + 1):
                print(f"Scraping page {current_page} of {max_pages}")

                # Get all apartment links on the current page
                hrefs = await getPageLinks(page)

                # Process each apartment
                await processApts(hrefs,apartmentsDf)

                # Check if there's a next page
                next_page_selector = "a.ant-pagination-item-link:has-text('>')"
                has_next = await page.query_selector(next_page_selector)
                # Check if the element was found AND we haven't reached max_pages
                if has_next and current_page < max_pages:
                    print("Navigating to the next page...")
                    await has_next.click()
                    await page.wait_for_load_state("networkidle", timeout=60000)
                else:
                    if not has_next:
                         print(f"No 'next page' element found using selector '{next_page_selector}' after page {current_page}.")
                    else: # current_page >= max_pages
                         print(f"Reached max_pages ({max_pages}). Stopping pagination.")
                    break # Exit the loop

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            await browser.close()

        return apartmentsDf


async def getPageLinks(page):
    hrefs = set()

    selector = config.LINKS_SELECTOR
    listing_container_selector = config.LISTING_CONTAINER_SELECTOR
    listing_container = await page.query_selector(listing_container_selector)

    if listing_container:
         apartment_links = await listing_container.query_selector_all(selector)
    else:
         print("Warning: Listing container not found, searching whole page.")
         apartment_links = await page.query_selector_all(selector)
    
    for link in apartment_links:
        href = await link.get_attribute('href')
        if href:
             # Construct full URL if relative
             if href.startswith('/'):
                 hrefs.add("https://fincaraiz.com.co" + href)
             elif href.startswith('http'):
                 hrefs.add(href)
    
    return hrefs

async def processApts(hrefs,apartmentsDf):
    scrapped_apts = set()

    for href in hrefs:
        # Get apartment info
        apartment_request = requests.get(href)
        print(f"Consulting {href}")

        aptPageHtml = apartment_request.text
        siteScrapping = BeautifulSoup(aptPageHtml, 'html.parser')
        next_data_script = siteScrapping.find('script', id='__NEXT_DATA__')

        if next_data_script:
            json_data = json.loads(next_data_script.string)
            apartment_data = getAptInfo(json_data)
            apartment_id = apartment_data.get('id', '')

            if apartment_id and (apartment_id not in scrapped_apts):
                apartmentsDf.loc[len(apartmentsDf)] = apartment_data
                print(f"Scraped apartment: {apartment_id}")
                scrapped_apts.add(apartment_id)

        # Add a small delay to avoid overloading the server
        await asyncio.sleep(1)