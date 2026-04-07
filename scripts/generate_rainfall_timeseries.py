import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

# Load new time-series data
df = pd.read_csv("C:/AI_Disaster_Project/data/rainfall_timeseries.csv")

rainfall = df["rainfall_mm"].values.reshape(-1, 1)

# Scale data
scaler = MinMaxScaler()
rainfall_scaled = scaler.fit_transform(rainfall)

# Create sequences
X = []
y = []

window = 5

for i in range(len(rainfall_scaled) - window):
    X.append(rainfall_scaled[i:i+window])
    y.append(rainfall_scaled[i+window])

X = np.array(X)
y = np.array(y)

print("X shape:", X.shape)
print("y shape:", y.shape)

# Build improved LSTM
model = Sequential([
    Input(shape=(window, 1)),
    LSTM(64, activation='relu'),
    Dense(1)
])

model.compile(
    optimizer='adam',
    loss='mse'
)

# Train
history = model.fit(
    X,
    y,
    epochs=30,
    batch_size=8,
    verbose=1
)

print("Flood LSTM model trained successfully.")

# Predict next day rainfall
last_sequence = rainfall_scaled[-window:]
last_sequence = last_sequence.reshape(1, window, 1)

prediction = model.predict(last_sequence)

predicted_rainfall = scaler.inverse_transform(prediction)

print("\nPredicted Next Day Rainfall:")
print(predicted_rainfall[0][0])

value = predicted_rainfall[0][0]

if value > 40:
    print("🔴 High Flood Risk")
elif value > 20:
    print("🟡 Medium Flood Risk")
else:
    print("🟢 Low Flood Risk")
