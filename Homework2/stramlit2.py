import streamlit as st
import numpy as np

# --------------------------
# MODEL WEIGHTS (Embedded)
# --------------------------
w0 = 0.01841801730804525
w = np.array([0.00015161, 0.00354204, -0.00500736, 0.01465133])

# --------------------------
# STREAMLIT UI
# --------------------------
st.title("🚗 Fuel Efficiency Prediction (MPG)")

st.write("Enter the vehicle details below to predict **Fuel Efficiency (Miles Per Gallon)**")

# Input fields (no min/max constraints)
engine_displacement = st.number_input("Engine Displacement (float)", format="%.4f")
horsepower = st.number_input("Horsepower (integer)", format="%d")
vehicle_weight = st.number_input("Vehicle Weight (float)", format="%.2f")
model_year = st.number_input("Model Year (integer)", format="%d")

# Prediction
if st.button("Predict"):
    features = np.array([engine_displacement, horsepower, vehicle_weight, model_year])
    y_pred = w0 + features.dot(w)
    st.success(f"Estimated Fuel Efficiency: **{y_pred:.2f} MPG**")
