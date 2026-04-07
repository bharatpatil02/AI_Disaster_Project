from sklearn.metrics import accuracy_score, f1_score
import numpy as np

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("🔥 Wildfire Model Validation")
print(f"Accuracy: {accuracy:.2f}")
print(f"F1 Score: {f1:.2f}")