import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Example actual vs predicted rainfall
y_true = np.array([25, 30, 35, 28, 40])
y_pred = np.array([27, 29, 34, 30, 38])

rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mae = mean_absolute_error(y_true, y_pred)

print("🌊 Flood Model Validation")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")