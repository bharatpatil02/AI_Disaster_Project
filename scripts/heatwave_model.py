import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# Load engineered dataset
df = pd.read_csv("C:/AI_Disaster_Project/data/featured_dataset.csv")

# Use Heat Index as target
y = df["Heat_Index"]

# Use only numeric features
X = df.select_dtypes(include=["number"]).drop(
    ["Heat_Index"], axis=1, errors="ignore"
)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Heatwave RMSE:", rmse)
print("Heatwave R2 Score:", r2)