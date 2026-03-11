import streamlit as st
import pandas as pd
import joblib
import os

# Load model safely
model_path = os.path.join(os.path.dirname(__file__), "delivery_risk_model.pkl")
model = joblib.load(model_path)

# Page config
st.set_page_config(page_title="Delivery Risk Predictor", layout="centered")

st.title("Delivery Risk Predictor")

st.write(
"""
This application predicts whether an e-commerce delivery will be **On-Time,
At-Risk, or Delayed** based on logistics features such as shipment distance,
seller reliability, warehouse processing time, traffic conditions, and weather.
"""
)

# ---------------- INPUT SECTION ----------------

order_volume = st.number_input("Order Volume", min_value=1, max_value=10, value=1)

processing_time = st.number_input(
    "Warehouse Processing Time (hours)", min_value=0.0, value=1.0
)

distance = st.number_input(
    "Shipment Distance (km)", min_value=0.0, value=5.0
)

seller_rating = st.slider(
    "Seller On-Time Rate",
    min_value=0.5,
    max_value=1.0,
    value=0.9,
    step=0.01
)

delivery_days = st.number_input(
    "Delivery Time (days)", min_value=1, value=2
)

traffic = st.selectbox(
    "Traffic Condition",
    ["Moderate", "Light"]
)

weather = st.selectbox(
    "Weather Condition",
    ["Normal", "Rainy"]
)

# ---------------- PREDICTION ----------------

if st.button("Predict Delivery Status"):

    data = {
        "order_volume": order_volume,
        "warehouse_processing_time_hours": processing_time,
        "shipment_distance_km": distance,
        "seller_on_time_rate": seller_rating,
        "delivery_time_days": delivery_days,
        "traffic_condition_Moderate": 1 if traffic == "Moderate" else 0,
        "traffic_condition_Light": 1 if traffic == "Light" else 0,
        "weather_indicator_Normal": 1 if weather == "Normal" else 0,
        "weather_indicator_Rainy": 1 if weather == "Rainy" else 0
    }

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    labels = ["At-Risk", "Delayed", "On-Time"]

    result = labels[prediction[0]]
    confidence = probability[0][prediction[0]] * 100

    st.success(f"Predicted Delivery Status: **{result}**")
    st.info(f"Prediction Confidence: **{confidence:.2f}%**")