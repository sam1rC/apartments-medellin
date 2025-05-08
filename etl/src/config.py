import pandas as pd

BASE_URL = "https://www.fincaraiz.com.co/venta/apartamentos/medellin/antioquia"
MAX_PAGES = 1
LINKS_SELECTOR = "a[href*='apartamento-en-venta']"
LISTING_CONTAINER_SELECTOR = "section.listingsWrapper"
NEXT_PAGE_SELECTOR = "a.ant-pagination-item-link:has-text('>')"