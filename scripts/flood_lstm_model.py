import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense # type: ignore

# Load data
df = pd.read_csv("C:/AI_Disaster_Project/data/featured_dataset.csv")

rainfall = df["rainfall_1h"].values.reshape(-1, 1)

# Scale
scaler = MinMaxScaler()
rainfall_scaled = scaler.fit_transform(rainfall)

# Create sequences
X = []
y = []

window = 3

for i in range(len(rainfall_scaled) - window):
    X.append(rainfall_scaled[i:i+window])
    y.append(rainfall_scaled[i+window])

X = np.array(X)
y = np.array(y)

# Build model
model = Sequential([
    LSTM(50, activation='relu', input_shape=(window, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Train
model.fit(X, y, epochs=50, verbose=1)

print("Flood LSTM model trained successfully.")