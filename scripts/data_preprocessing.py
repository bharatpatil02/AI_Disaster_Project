import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

weather_df = pd.read_csv("C:/AI_Disaster_Project/data/weather_data.csv")
disaster_df = pd.read_csv("C:/AI_Disaster_Project/data/clean_disaster_data.csv")

print("Weather Shape:", weather_df.shape)
print("Disaster Shape:", disaster_df.shape)

merged_df = pd.concat([weather_df, disaster_df], axis=1)

merged_df = merged_df.fillna("0")

label_encoder = LabelEncoder()

# Convert categorical columns to string first
if "weather_condition" in merged_df.columns:
    merged_df["weather_condition"] = merged_df["weather_condition"].astype(str)
    merged_df["weather_condition"] = label_encoder.fit_transform(
        merged_df["weather_condition"]
    )

if "Disaster Type" in merged_df.columns:
    merged_df["Disaster Type"] = merged_df["Disaster Type"].astype(str)
    merged_df["Disaster Type"] = label_encoder.fit_transform(
        merged_df["Disaster Type"]
    )

# Normalize numeric columns
numeric_cols = [
    "temperature",
    "humidity",
    "pressure",
    "wind_speed",
    "rainfall_1h",
    "Total Deaths",
    "Total Affected"
]

numeric_cols = [col for col in numeric_cols if col in merged_df.columns]

scaler = StandardScaler()
merged_df[numeric_cols] = scaler.fit_transform(merged_df[numeric_cols])

merged_df.to_csv(
    "C:/AI_Disaster_Project/data/preprocessed_dataset.csv",
    index=False
)

print("\nPreprocessed Data:")
print(merged_df.head())

print("\nShape:", merged_df.shape)