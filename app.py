import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import datetime
import joblib

try:
    model = load_model('earthquake_prediction_model.keras')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

try:
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    st.error(f"Error loading scaler: {e}")
    st.stop()

st.title('Earthquake Depth and Magnitude Prediction')

st.write("""This application predicts the depth and magnitude of an earthquake
         based on the provided geological and temporal information.""")

st.header('Input Features')

latitude = st.slider('Latitude', min_value=-90.0, max_value=90.0, value=0.0, step=0.001)
longitude = st.slider('Longitude', min_value=-180.0, max_value=180.0, value=0.0, step=0.001)

date_input = st.date_input('Date', datetime.date.today())
time_input = st.time_input('Time', datetime.datetime.now().time())

year = date_input.year
month = date_input.month
day = date_input.day
hours = time_input.hour
minutes = time_input.minute
seconds = time_input.second

input_data = np.array([[latitude, longitude, minutes, hours, seconds, year, month, day]])
scaled_input_data = scaler.transform(input_data)
prediction = model.predict(scaled_input_data)

st.subheader('Prediction Results')
st.write(f"Predicted Depth: {prediction[0][0]:.2f}")
st.write(f"Predicted Magnitude: {prediction[0][1]:.2f}")