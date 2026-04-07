import requests
import pandas as pd

API_KEY = "572d89b2daf72aeb869b075be8690718"

cities = ["Nashik", "Mumbai", "Pune", "Nagpur"]

weather_data = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    rainfall = data.get("rain", {}).get("1h", 0)

    weather_info = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "weather_condition": data["weather"][0]["main"],
        "rainfall_1h": rainfall
    }

    weather_data.append(weather_info)

df = pd.DataFrame(weather_data)

df.to_csv("C:/AI_Disaster_Project/data/weather_data.csv", index=False)

print(df)