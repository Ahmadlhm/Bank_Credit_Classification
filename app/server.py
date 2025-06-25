from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib


model = joblib.load('app/best_credit_score_model.pkl')

class_names = np.array(['Poor', 'Standard', 'Good'])
app = FastAPI()

class InputData(BaseModel):
    features: list

@app.get('/')
def read_root():
    return {'message': 'Bank Credit Classification model API'}
@app.post('/predict')
def predict(data: InputData):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {'predicted_class': class_names[int(prediction[0])]}


