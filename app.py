import streamlit as st
import pandas as pd
import joblib

model = joblib.load("delivery_risk_model.pkl")

st.title("Delivery Risk Predictor")

st.write(
"""
This application predicts whether an e-commerce delivery will be
**On-Time, At-Risk, or Delayed** based on logistics features such as
shipment distance, seller reliability, warehouse processing time,
traffic conditions, and weather.
"""
)


order_volume = st.number_input("Order Volume", 1, 10)
processing_time = st.number_input("Warehouse Processing Time (hours)", 0.0)
distance = st.number_input("Shipment Distance (km)", 0.0)
seller_rate = st.slider("Seller On-Time Rate", 0.0, 1.0)
delivery_days = st.number_input("Delivery Time (days)", 1)

traffic = st.selectbox("Traffic Condition", ["Moderate", "Light"])
weather = st.selectbox("Weather", ["Normal", "Rainy"])

if st.button("Predict Delivery Status"):

    data = {
        "order_volume": order_volume,
        "warehouse_processing_time_hours": processing_time,
        "shipment_distance_km": distance,
        "seller_on_time_rate": seller_rate,
        "delivery_time_days": delivery_days,
        "traffic_condition_Moderate": 1 if traffic == "Moderate" else 0,
        "traffic_condition_Light": 1 if traffic == "Light" else 0,
        "weather_indicator_Normal": 1 if weather == "Normal" else 0,
        "weather_indicator_Rainy": 1 if weather == "Rainy" else 0
    }

    input_df = pd.DataFrame([data])

prediction = model.predict(input_df)

# map encoded values back to labels
labels = ["At-Risk", "Delayed", "On-Time"]

result = labels[prediction[0]]

st.success(f"Predicted Delivery Status: {result}")
