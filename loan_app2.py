# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 22:37:41 2025

@author: ADMIN
"""

import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('loan_default_risk.pkl', 'rb') as f:
    model = pickle.load(f)

# App Title
st.title("Loan Default Risk Predictor")
st.markdown(
    "Use this tool to assess the **risk of default** for a loan applicant based on their financial and personal background."
)

st.divider()

# Collect user input
st.header("Applicant Information")

totaldue = st.number_input(
    label="Total Amount Due (₦)",
    min_value=10000.0,
    max_value=70000.0,
    value=10000.0,
    step=500.0
)

termdays = st.slider(
    label="Term Duration (Days)",
    min_value=0.0,
    max_value=30.0,
    value=5.0
)

loan_to_due_ratio = st.slider(
    label="Loan-to-Due Ratio",
    min_value=0.0,
    max_value=1.5,
    value=0.5,
    step=0.05
)

employment_status_clients = st.selectbox(
    label="Employment Status",
    options=["Self-Employed", "Student", "Unemployed", "Retired", "Contract"]
)

level_of_education_clients = st.selectbox(
    label="Educational Attainment",
    options=["Primary", "Secondary", "Graduate", "Post-Graduate"]
)

age = st.slider(
    label="Applicant Age",
    min_value=18.0,
    max_value=100.0,
    value=30.0,
    step=1.0
)

# Submit button
st.divider()
if st.button("🔍 Predict Loan Default Risk"):
    # Create input dataframe
    input_data = {
        'totaldue': [totaldue],
        'termdays': [termdays],
        'loan_to_due_ratio': [loan_to_due_ratio],
        'employment_status_clients': [employment_status_clients],
        'level_of_education_clients': [level_of_education_clients],
        'age': [age]
    }

    input_df = pd.DataFrame(input_data)

    # Generate prediction
    prediction = model.predict(input_df)[0]

    # Display result
    st.subheader("Prediction Result")
    if prediction == 1:
        st.error("The applicant is **likely to default** on the loan.")
    else:
        st.success("The applicant is **not likely to default** on the loan.")

