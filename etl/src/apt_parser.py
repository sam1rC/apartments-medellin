def parseAptInfo(rawAptData: dict) -> dict:
  props = rawAptData.get("props")

  aptData = {
        "id" : None,
        "amount" : None,
        "latitude" : None,
        "longitude" : None,
        "bathrooms" : None,
        "bedrooms" : None,
        "garage" : None,
        "stratum" : None,
        "m2Terrain" : None
    }

  if not props:
    return aptData
  
  pageProps = props.get("pageProps", {})
  data = pageProps.get("data", {})

  if not data:
    return aptData
  
  price_info = data.get("price",{})
  technicalSheet = data.get("technicalSheet",{})

  aptData["amount"] = price_info.get("amount",None)
  aptData["latitude"] = data.get("latitude",None)
  aptData["longitude"] = data.get("longitude",None)
  aptData["id"] = data.get("id",None)

  technicalSheetTargetFields = {"bathrooms","bedrooms","garage","stratum","m2Terrain"}

  for item in technicalSheet:
    fieldName = item.get("field")
    value = item.get("value")

    if fieldName in technicalSheetTargetFields:
      if fieldName == "m2Terrain" and value:
        aptData[fieldName] = getM2Value(value)
      elif fieldName == "m2Terrain":
        aptData["m2Terrain"] = data.get("m2")
      else:
        aptData[fieldName] = value

  return aptData
  
def getM2Value(m2String) -> float:
  splittedM2String = m2String.split(' ')

  if splittedM2String:
    return float(splittedM2String[0])
  return None