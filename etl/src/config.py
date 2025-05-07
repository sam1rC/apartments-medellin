import pandas as pd

BASE_URL = "https://www.fincaraiz.com.co/venta/apartamentos/medellin/antioquia"
MAX_PAGES = 1
APARTMENTS_DF_COLUMNS = ["id","amount","latitude","longitude","m2","stratum","bathrooms","bedrooms","garage"]
LINKS_SELECTOR = "a[href*='apartamento-en-venta']"
LISTING_CONTAINER_SELECTOR = "section.listingsWrapper"