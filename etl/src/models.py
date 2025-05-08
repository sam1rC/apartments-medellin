from typing import Optional, Union
from pydantic import BaseModel, Field

class ApartmentData(BaseModel):
    id: Optional[int] = Field(None, description="Unique identifier for the property.")
    amount: Optional[Union[int, float]] = Field(None, description="The price or value of the property.")
    latitude: Optional[float] = Field(None, description="Latitude of the property.")
    longitude: Optional[float] = Field(None, description="Longitude of the property.")
    stratum: Optional[int] = Field(None, description="Socioeconomic stratum of the property.")
    bathrooms: Optional[int] = Field(None, description="Number of bathrooms.")
    m2Terrain: Optional[float] = Field(None, alias="m2Terrain", description="Terrain area in square meters.")
    bedrooms: Optional[int] = Field(None, description="Number of bedrooms.")
    garage: Optional[int] = Field(None, description="Number of garage spaces.")
