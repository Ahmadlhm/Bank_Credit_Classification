from fastapi import FastAPI
import joblib
import numpy as np


model = joblib.load('app/rf.joblib')

class_names = np.array(['Poor', 'Standard', 'Good'])

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Bank Credit Classification model API'}

@app.post('/predict')
def predict(data: dict):
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'predicted_class': class_name}