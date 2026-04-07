import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

y_true = [1, 0, 1, 1, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1]

disp = ConfusionMatrixDisplay.from_predictions(y_true, y_pred)
plt.title("🔥 Wildfire Confusion Matrix")
plt.show()

