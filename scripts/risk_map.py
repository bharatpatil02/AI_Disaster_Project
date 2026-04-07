import pandas as pd
import folium

df = pd.read_csv("C:/AI_Disaster_Project/data/predictions.csv")

# Create base map centered on Maharashtra
risk_map = folium.Map(location=[19.5, 75.0], zoom_start=6)

for _, row in df.iterrows():
    if row["Severity"] == "High":
        color = "red"
    elif row["Severity"] == "Medium":
        color = "orange"
    else:
        color = "green"

    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Region']} - {row['Disaster_Type']} ({row['Severity']})",
        icon=folium.Icon(color=color)
    ).add_to(risk_map)

risk_map.save("C:/AI_Disaster_Project/data/risk_map.html")

print("Risk map created successfully.")