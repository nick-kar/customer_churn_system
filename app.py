import streamlit as st
import numpy as np
import tensorflow as tf
import joblib
import pandas as pd

# -----------------------
# LOAD MODEL + SCALER
# -----------------------
model = tf.keras.models.load_model("models/churn_model.keras")
scaler = joblib.load("models/scaler.pkl")

st.title("📊 Customer Churn Prediction System")

st.write("Enter customer data to predict churn probability.")

# -----------------------
# USER INPUTS
# -----------------------
tenure = st.number_input("Tenure (months)", 0, 100, 1)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 500.0)

# create 45-feature vector expected by scaler/model
input_data = np.zeros((1, 45))

# put demo values into first positions
input_data[0, 0] = tenure
input_data[0, 1] = monthly
input_data[0, 2] = total

# scale
input_data = scaler.transform(input_data)

# prediction
if st.button("Predict Churn"):
    prob = model.predict(input_data)[0][0]
    
    st.write(f"### Churn Probability: {prob:.2f}")

    if prob > 0.5:
        st.error("⚠ Customer likely to churn")
    else:
        st.success("✔ Customer likely to stay")