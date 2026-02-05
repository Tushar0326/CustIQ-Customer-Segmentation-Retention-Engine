import streamlit as st
import requests

st.title("CustIQ Customer Churn Dashboard")

st.subheader("Enter Customer Behavior")

recency = st.number_input("Recency (days since last purchase)", min_value=0)
frequency = st.number_input("Purchase Frequency", min_value=0)
monetary = st.number_input("Total Spend", min_value=0.0)
cluster = st.number_input("Cluster ID", min_value=0)

if st.button("Predict Churn"):

    data = {
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary,
        "Cluster": cluster
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.success(f"Churn Prediction: {result['Churn Prediction']}")
    st.warning(f"Churn Probability: {result['Churn Probability']:.2f}")
