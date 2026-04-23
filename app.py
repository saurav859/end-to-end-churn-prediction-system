
import streamlit as st
import pandas as pd
import joblib # Changed from skops.io to joblib
import numpy as np

# Load the trained model pipeline
# The pipeline includes preprocessing steps and the XGBoost model
model = joblib.load('churn_model.joblib') # Changed from sio.load to joblib.load

st.title('Telco Customer Churn Prediction')
st.write('Enter customer details to predict churn.')

# Define the input fields based on the DataFrame columns excluding 'Churn'
# Ensure the order and type match the training data

gender = st.selectbox('Gender', ['Female', 'Male'])
SeniorCitizen = st.selectbox('Senior Citizen', [0, 1])
Partner = st.selectbox('Partner', ['Yes', 'No'])
Dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.slider('Tenure (months)', 0, 72, 1)
PhoneService = st.selectbox('Phone Service', ['Yes', 'No'])
MultipleLines = st.selectbox('Multiple Lines', ['No phone service', 'No', 'Yes'])
InternetService = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.selectbox('Online Security', ['No', 'Yes', 'No internet service'])
OnlineBackup = st.selectbox('Online Backup', ['No', 'Yes', 'No internet service'])
DeviceProtection = st.selectbox('Device Protection', ['No', 'Yes', 'No internet service'])
TechSupport = st.selectbox('Tech Support', ['No', 'Yes', 'No internet service'])
StreamingTV = st.selectbox('Streaming TV', ['No', 'Yes', 'No internet service'])
StreamingMovies = st.selectbox('Streaming Movies', ['No', 'Yes', 'No internet service'])
Contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox('Paperless Billing', ['Yes', 'No'])
PaymentMethod = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
MonthlyCharges = st.slider('Monthly Charges', 18.0, 120.0, 50.0)
TotalCharges = st.slider('Total Charges', 0.0, 9000.0, 1000.0)

# Create a DataFrame from the input data
input_data = pd.DataFrame([{
    'gender': gender,
    'SeniorCitizen': SeniorCitizen,
    'Partner': Partner,
    'Dependents': Dependents,
    'tenure': tenure,
    'PhoneService': PhoneService,
    'MultipleLines': MultipleLines,
    'InternetService': InternetService,
    'OnlineSecurity': OnlineSecurity,
    'OnlineBackup': OnlineBackup,
    'DeviceProtection': DeviceProtection,
    'TechSupport': TechSupport,
    'StreamingTV': StreamingTV,
    'StreamingMovies': StreamingMovies,
    'Contract': Contract,
    'PaperlessBilling': PaperlessBilling,
    'PaymentMethod': PaymentMethod,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges
}])

if st.button('Predict Churn'):
    prediction_proba = model.predict_proba(input_data)[:, 1]
    prediction = model.predict(input_data)[0]

    churn_status = 'Yes' if prediction == 1 else 'No'
    st.subheader(f'Prediction: Customer will Churn: {churn_status}')
    st.write(f'Churn Probability: {prediction_proba[0]:.2f}')

    if prediction == 1:
        st.warning('This customer is likely to churn!')
    else:
        st.success('This customer is likely to stay.')
