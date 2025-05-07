import asyncio
import config
import pandas as pd
from extractor import scrapeApartments


async def main():
    # Base URL and pagination setup
    base_url = config.BASE_URL
    max_pages = config.MAX_PAGES

    scrappedApts = await scrapeApartments(base_url,max_pages)

    scrappedApts.to_csv("../data/apt_data.csv", encoding='utf-8', index=False)

if __name__ == "__main__":
    asyncio.run(main())