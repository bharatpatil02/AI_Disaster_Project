import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("C:/AI_Disaster_Project/data/featured_dataset.csv")

X = df[["temperature", "humidity", "wind_speed", "Heat_Index", "Combined_Risk"]]
y = df["Heat_Index"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "C:/AI_Disaster_Project/models/heatwave_model.pkl")

print("Model saved successfully.")