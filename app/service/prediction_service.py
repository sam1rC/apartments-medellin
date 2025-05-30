from joblib import load
from domain.domain_model import ApartmentData

class PredictionService:
    def __init__(self,model_path: str):
        self._model_path = model_path
        self._model = None
        self._load_model()

    def _load_model(self):
        """ Load the joblib model """
        try:
            self._model = load(self._model_path)
        except Exception as e:
            raise Exception(f"Failed load model: {str(e)}")
        
    def execute(self,data: ApartmentData):
        df = data.to_df()
        predicted_price = self._model.predict(df)
        return predicted_price[0]