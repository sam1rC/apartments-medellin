from fastapi import FastAPI
from joblib import load
from typing import Optional, Union
from pydantic import BaseModel, Field
import numpy as np
import pandas as pd

class ApartmentData(BaseModel):
    latitude: Optional[float] = Field(None, description="Latitude of the property.")
    longitude: Optional[float] = Field(None, description="Longitude of the property.")
    stratum: Optional[int] = Field(None, description="Socioeconomic stratum of the property.")
    bathrooms: Optional[int] = Field(None, description="Number of bathrooms.")
    m2Terrain: Optional[float] = Field(None, alias="m2Terrain", description="Terrain area in square meters.")
    bedrooms: Optional[int] = Field(None, description="Number of bedrooms.")
    garage: Optional[int] = Field(None, description="Number of garage spaces.")

    def to_df(self):
        """Convert the model data to numpy array for prediction"""
        return pd.DataFrame({
            'latitude': [self.latitude],
            'longitude': [self.longitude],
            'stratum': [self.stratum],
            'bathrooms': [self.bathrooms],
            'm2Terrain': [self.m2Terrain],
            'bedrooms': [self.bedrooms],
            'garage': [self.garage]
        })

app = FastAPI()

model = load(r"../models/rf-model.joblib")

print(model)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict_apt_price(apt: ApartmentData):
    apt_data = apt.to_df()
    prediction = model.predict(apt_data)
    return prediction[0]
