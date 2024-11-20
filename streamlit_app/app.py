import streamlit as st
import requests

st.title("Commercial Real Estate Prediction")

# Input fields
area = st.number_input("Area (sq ft)")
growth_rate = st.number_input("Growth Rate")
# Additional fields...

if st.button("Predict"):
    data = {"area": area, "growth_rate": growth_rate}
    response = requests.post("http://127.0.0.1:8000/predict/", json=data)
    st.write(response.json())