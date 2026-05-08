# 🌍 AI-Powered Climate Disaster Prediction & Response System

An end-to-end Artificial Intelligence and Machine Learning based disaster prediction system designed to predict and monitor Floods, Wildfires, and Heatwaves using climate data, satellite imagery, and historical disaster records.

This project combines Deep Learning, Machine Learning, Geospatial Analysis, APIs, and Real-Time Visualization to provide early warning alerts and disaster risk monitoring.

---

# 🚀 Project Overview

The system collects weather and environmental data from multiple sources, preprocesses and engineers important climate features, trains AI/ML models, generates predictions, and visualizes disaster-prone regions through interactive dashboards and maps.

The main goal of this project is to help governments, NGOs, and disaster management authorities take preventive action before disasters occur.

---

# 🎯 Features

✅ Flood Prediction using LSTM  
✅ Wildfire Prediction using CNN  
✅ Heatwave Prediction using Random Forest  
✅ Real-Time Disaster Alerts  
✅ Interactive Risk Maps  
✅ Streamlit Dashboard  
✅ Satellite Image Processing  
✅ Feature Engineering for Climate Risk  
✅ Visualization & Monitoring System  
✅ Deployment Ready Architecture

---

# 🧠 AI/ML Models Used

## 🌊 Flood Prediction
- Model: LSTM (Long Short-Term Memory)
- Purpose: Predict future rainfall and flood risk using time-series data.

### Features Used
- Rainfall
- Humidity
- Pressure
- Water-related climate trends

### Output
- Next-day rainfall prediction
- Flood risk classification:
  - Low Risk
  - Medium Risk
  - High Risk

---

## 🔥 Wildfire Prediction
- Model: CNN (Convolutional Neural Network)
- Purpose: Detect wildfire-prone regions using satellite imagery.

### Features Used
- NDVI
- Temperature
- Wind Speed
- Vegetation Stress
- Land Cover

### Output
- Wildfire risk classification
- Spatial fire risk detection

---

## 🌡 Heatwave Prediction
- Model: Random Forest Regression
- Purpose: Predict heatwave intensity and temperature anomalies.

### Features Used
- Temperature
- Humidity
- Heat Index
- Pressure
- Historical Heatwave Data

### Output
- Heatwave risk score
- Temperature anomaly prediction

---

# 🛰 Data Sources & APIs

## Weather & Climate Data
- OpenWeatherMap API
- NASA POWER API
- NOAA Climate Data

## Satellite Imagery
- Google Earth Engine
- NASA MODIS Dataset
- Landsat Imagery

## Historical Disaster Data
- EM-DAT Dataset
- CSV Disaster Records

---

# ⚙️ Tech Stack

| Layer | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow, Keras |
| Visualization | Matplotlib, Seaborn, Plotly |
| Mapping | Folium, Google Earth Engine |
| Dashboard | Streamlit |
| Deployment | Flask, Docker, AWS/GCP |
| APIs | OpenWeatherMap API, NASA APIs |

---

# 📂 Project Structure

```bash
AI_Disaster_Project/
│
├── data/
│   ├── weather_data.csv
│   ├── preprocessed_dataset.csv
│   ├── featured_dataset.csv
│   ├── rainfall_timeseries.csv
│   ├── predictions.csv
│   └── satellite_images.tif
│
├── models/
│   ├── flood_lstm_model.h5
│   ├── wildfire_cnn_model.h5
│   └── heatwave_model.pkl
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── flood_lstm_model.py
│   ├── wildfire_cnn_model.py
│   ├── heatwave_model.py
│   ├── risk_map.py
│   ├── alerts.py
│   └── confusion_matrix_plot.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🔄 Project Workflow

```text
Data Collection
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Model Development
        ↓
Prediction Generation
        ↓
Alert System
        ↓
Risk Visualization Dashboard
        ↓
Deployment
```

---

# 🧹 Data Preprocessing

Performed:
- Data Cleaning
- Missing Value Handling
- Label Encoding
- Feature Scaling
- Dataset Merging

Generated:
```bash
preprocessed_dataset.csv
```

---

# 🧪 Feature Engineering

Created advanced climate risk features:

- Heat Index
- Rainfall Anomaly
- Fire Risk Score
- Pressure Anomaly
- Combined Risk Score

Generated:
```bash
featured_dataset.csv
```

---

# 📊 Model Evaluation

## Heatwave Prediction
- RMSE: 0.203
- R² Score: 0.974

## Flood Prediction
- LSTM trained successfully on rainfall time-series data.

## Wildfire Prediction
- CNN model successfully classified wildfire risk.

---

# 🚨 Alert System

The system generates automatic alerts for high-risk regions.

### Example Alerts

```text
⚠ Flood HIGH risk in Pune | Probability: 0.78
⚠ Wildfire HIGH risk in Nagpur | Probability: 0.81
```

---

# 🗺 Risk Map Visualization

Interactive disaster risk maps were created using Folium.

### Risk Colors
- 🟥 Red → High Risk
- 🟧 Orange → Medium Risk
- 🟩 Green → Low Risk

Generated:
```bash
risk_map.html
```

---

# 📈 Streamlit Dashboard

The dashboard displays:

- Live disaster alerts
- Risk maps
- Prediction statistics
- Severity distribution
- Real-time monitoring interface

Run Dashboard:

```bash
streamlit run app.py
```

---

# 🖥 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI_Disaster_Project.git
```

---

## 2️⃣ Navigate to Project

```bash
cd AI_Disaster_Project
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

## Data Preprocessing

```bash
python scripts/data_preprocessing.py
```

## Feature Engineering

```bash
python scripts/feature_engineering.py
```

## Train Heatwave Model

```bash
python scripts/heatwave_model.py
```

## Train Flood LSTM Model

```bash
python scripts/flood_lstm_model.py
```

## Train Wildfire CNN Model

```bash
python scripts/wildfire_cnn_model.py
```

## Generate Risk Map

```bash
python scripts/risk_map.py
```

## Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 🌍 Real-World Applications

- Disaster Management Systems
- Government Climate Monitoring
- Flood Early Warning Systems
- Wildfire Monitoring
- Heatwave Forecasting
- Smart City Disaster Planning

---

# 🔮 Future Enhancements

- IoT Sensor Integration
- Drone-Based Monitoring
- Live Satellite Streaming
- SMS & Email Alert System
- Mobile Application
- Earthquake & Cyclone Prediction
- Reinforcement Learning Models

---

# 🎯 Project Outcome

This project demonstrates how Artificial Intelligence and Deep Learning can be used for:

- Climate Risk Prediction
- Disaster Preparedness
- Early Warning Systems
- Real-Time Monitoring
- Data-Driven Decision Making

---

# 👨‍💻 Developed By

## Bharat Patil
AI / ML Developer | Cybersecurity Enthusiast

---

# 📜 License

This project is developed for educational and research purposes.
