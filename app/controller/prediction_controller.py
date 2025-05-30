from domain.domain_model import ApartmentData
from service.prediction_service import PredictionService
from fastapi import APIRouter
from config import MODEL_PATH

router = APIRouter()

@router.post("/predict")
def handle_prediction(data: ApartmentData):
    prediction_service = PredictionService(MODEL_PATH)
    prediction = prediction_service.execute(data)
    return prediction