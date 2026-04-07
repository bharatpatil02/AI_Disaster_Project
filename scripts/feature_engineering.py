import pandas as pd
import numpy as np

# Load preprocessed data
df = pd.read_csv("C:/AI_Disaster_Project/data/preprocessed_dataset.csv")

print("Original Shape:", df.shape)

# --------------------------------------------------
# 1. Heat Index (simple approximation)
# HI = temperature + humidity effect
# --------------------------------------------------
df["Heat_Index"] = (
    df["temperature"] + 0.1 * df["humidity"]
)

# --------------------------------------------------
# 2. Rainfall Anomaly
# Current rainfall - average rainfall
# --------------------------------------------------
avg_rainfall = df["rainfall_1h"].mean()
df["Rainfall_Anomaly"] = (
    df["rainfall_1h"] - avg_rainfall
)

# --------------------------------------------------
# 3. Fire Weather Risk
# Based on temperature + wind - humidity
# --------------------------------------------------
df["Fire_Risk_Score"] = (
    df["temperature"] * 0.5 +
    df["wind_speed"] * 0.3 -
    df["humidity"] * 0.2
)

# --------------------------------------------------
# 4. Pressure anomaly
# --------------------------------------------------
avg_pressure = df["pressure"].mean()
df["Pressure_Anomaly"] = (
    df["pressure"] - avg_pressure
)

# --------------------------------------------------
# 5. Combined Disaster Risk Feature
# --------------------------------------------------
df["Combined_Risk"] = (
    df["Heat_Index"] +
    df["Rainfall_Anomaly"] +
    df["Fire_Risk_Score"]
)

# Save final dataset
df.to_csv(
    "C:/AI_Disaster_Project/data/featured_dataset.csv",
    index=False
)

print("\nNew Shape:", df.shape)
print("\nNew Columns Added:")
print(df.columns)

print("\nPreview:")
print(df.head())

