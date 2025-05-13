import asyncio
import config
from extractor import scrapeApartments
from loaders import loadAptData

async def main():
    # Base URL and pagination setup
    base_url = config.BASE_URL
    max_pages = config.MAX_PAGES

    scrappedApts = await scrapeApartments(base_url,max_pages)

    aptsDf = loadAptData(scrappedApts)

    aptsDf.to_csv('../data/apt_data_test.csv',encoding='utf-8',index=False)


if __name__ == "__main__":
    asyncio.run(main())