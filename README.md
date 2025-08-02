# 🌍 GeoQuakePredict - AI-powered Earthquake Impact Predictor

---

## 🔍 Project Goal

GeoQuakePredict aims to **predict the depth and magnitude of earthquakes** based on geological coordinates and temporal attributes using a trained deep learning model. This can assist researchers and disaster response planners in identifying potential impacts of seismic events.

---

## 📌 Project Overview

This project involves building a regression-based deep learning model that takes in user-defined inputs like latitude, longitude, and timestamp to forecast two key earthquake parameters: **Depth** (in km) and **Magnitude** (Richter scale).  
The model is deployed using **Streamlit**, allowing for a responsive and user-friendly prediction interface.

---

## 🔁 Project Workflow

### 📊 1. Data Preprocessing
- Loaded the earthquake dataset containing features such as `latitude`, `longitude`, `date`, and `time`.
- Extracted relevant time-based features: `year`, `month`, `day`, `hour`, `minute`, `second`.
- Handled missing/null values.
- Standardized the input features using `StandardScaler` to normalize the data for efficient training.
- Split the data into **training** and **testing** sets (80:20 split).

### 🤖 2. Model Building
- Built a **Deep Learning model using TensorFlow and Keras**.
- Model architecture:
  - Input layer: 8 features
  - Hidden layers: Multiple Dense layers with ReLU activation
  - Output layer: 2 neurons (for Depth and Magnitude)
- Used **Mean Squared Error (MSE)** as the loss function and **Adam** optimizer.
- Trained the model over several epochs to minimize prediction errors.

### ✅ 3. Evaluation Metrics
- Evaluated the model using:
  - **Mean Absolute Error (MAE)**
  - **Root Mean Squared Error (RMSE)**
- Achieved:
  - **MAE (Depth): ~11.28**
  - **MAE (Magnitude): ~0.15**
- The low MAE values indicate strong prediction performance for both outputs.

### 🌐 4. Deployment
- Built an interactive web interface using **Streamlit**.
- Accepts user inputs for:
  - Latitude
  - Longitude
  - Date
  - Time
- Performs scaling using the saved `StandardScaler` (`scaler.pkl`) and loads the trained model (`earthquake_prediction_model.keras`).
- Displays:
  - **Predicted Depth**
  - **Predicted Magnitude**

---

## 🧰 Tech Stack

### 📌 Programming Language
- Python 3.x

### 🧠 Machine Learning & Deep Learning
- TensorFlow / Keras
- scikit-learn

### 📊 Data Manipulation & Visualization
- pandas
- numpy
- matplotlib
- seaborn

### 🌐 Deployment
- Streamlit
- joblib (for scaler serialization)

---

## 📁 Project Structure

```
GeoQuakePredict/
├── dataset/
│   └── database.csv                   # Raw dataset used for training
├── .gitignore                         # Files/directories to exclude from Git tracking
├── Earthquake_Prediction.ipynb        # Jupyter notebook for data processing and model training
├── LICENSE                            # Allows reuse, with attribution, no warranty
├── README.md                          # Project documentation
├── app.py                             # Streamlit web app for live predictions
├── earthquake_prediction_model.keras  # Trained deep learning model saved in Keras format
├── requirements.txt                   # Python dependencies
└── scaler.pkl                         # Pre-fitted StandardScaler object for input normalization

```


---

## ✨ Features

- 🌐 **Web App Interface** – Built with Streamlit for fast and interactive predictions.
- 📍 **Geographical Input** – Takes in latitude and longitude.
- 🕒 **Temporal Input** – Accepts date and time values.
- 📈 **Dual Output Prediction** – Simultaneously predicts **depth** and **magnitude**.
- 🧠 **Deep Learning Model** – Powered by TensorFlow, trained on real-world seismic data.
- ⚙️ **Preprocessing Included** – Scales and formats inputs behind the scenes.

---

## 🚀 Future Enhancements

- 🌍 Add **map visualizations** for predicted earthquake locations.
- 🧮 Integrate **uncertainty estimation** with confidence ranges.
- 🛎️ Enable **risk alert system** based on thresholds.
- 🔍 Improve generalization using larger or global datasets.
- 📡 Add **real-time data ingestion** from earthquake monitoring APIs.

---

## 🧪 How to Run Locally

```
git clone https://github.com/yourusername/GeoQuakePredict.git
cd GeoQuakePredict
pip install -r requirements.txt
streamlit run app.py
```
---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀 

