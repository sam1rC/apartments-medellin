from fastapi import FastAPI
from controller.prediction_controller import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message":"This is the apartment princing prediction API"}
