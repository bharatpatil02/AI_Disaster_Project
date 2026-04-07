from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

y_true = np.array([38, 40, 42, 39, 41])
y_pred = np.array([37.8, 40.2, 41.7, 39.5, 40.8])

r2 = r2_score(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))

print("🌡 Heatwave Model Validation")
print(f"R2 Score: {r2:.3f}")
print(f"RMSE: {rmse:.3f}")