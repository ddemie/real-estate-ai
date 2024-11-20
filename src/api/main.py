from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.post("/predict/")
async def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction[0]}