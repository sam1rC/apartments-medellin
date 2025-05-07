from bs4 import BeautifulSoup

def getAptInfo(aptData):
  props = aptData.get("props")
  if props:
    page_props = props.get("pageProps", {})
    data = page_props.get("data", {})

    price = data.get("price",{})
    technicalSheet = data.get("technicalSheet",{})

    amount = price.get("amount","")
    latitude = data.get("latitude","")
    longitude = data.get("longitude","")
    m2 = data.get("m2","")
    id = data.get("id","")

    technicalSheetItems = ["bathrooms","bedrooms","garage","stratum"]

    aptData = {
        "id" : id,
        "amount" : amount,
        "latitude" : latitude,
        "longitude" : longitude,
        "m2" : m2
    }

    for item in technicalSheet:
      field = item["field"]
      if field in technicalSheetItems:
        aptData[field] = item["value"]

    return aptData