# 🌍 GeoQuakePredict

**AI-powered Earthquake Impact Predictor**

---

## 🔍 Project Goal

GeoQuakePredict is designed to **predict the depth and magnitude of earthquakes** using geological and temporal data inputs. By leveraging machine learning and deep learning models, this project aims to provide early insights that could contribute to disaster preparedness and risk mitigation.

---

## 📌 Project Overview

Earthquakes are unpredictable natural phenomena, but with the right historical data and machine learning techniques, we can forecast critical parameters like **depth** and **magnitude** with reasonable accuracy.  
GeoQuakePredict allows users to input parameters such as latitude, longitude, date, and time, and provides predictions through a deployed web app interface.

---

## 🔁 Project Workflow

### 📊 1. Data Preprocessing
- Cleaned and normalized data
- Extracted temporal features (year, month, day, hour, minute, second)
- Applied feature scaling using `StandardScaler`

### 🤖 2. Model Building
- Tested multiple models: Linear Regression, Random Forest, and Deep Neural Network
- Final model: **Deep Learning (Keras Sequential)**
- Trained to predict two outputs: **Depth** and **Magnitude**

### ✅ 3. Evaluation Metrics
- Metrics used: **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**
- Achieved low error values, indicating reliable predictions

### 🌐 4. Deployment
- Deployed using **Streamlit**
- Interactive sliders and date/time pickers for user input
- Real-time prediction displayed on the interface

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend/Modeling**:
  - Python
  - TensorFlow / Keras
  - Scikit-learn
  - NumPy
  - Pandas
- **Visualization**:
  - Matplotlib
  - Seaborn
- **Utilities**:
  - Joblib (for model/scaler serialization)

---

## 📁 Project Structure

