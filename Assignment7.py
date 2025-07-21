import streamlit as st
import joblib

# Load the model
model = joblib.load('model.pkl')

st.title("ML Model Predictor")

# Collect user inputs
user_input1 = st.number_input("Feature 1")
user_input2 = st.number_input("Feature 2")
user_input3 = st.number_input("Feature 3")
user_input4 = st.number_input("Feature 4")

# Add more inputs if needed based on the number of features your model expects

# Predict when button is clicked
if st.button("Predict"):
    prediction = model.predict([[user_input1, user_input2, user_input3, user_input4]])
    st.write("Prediction:", prediction)


