import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("C:/AI_Disaster_Project/data/preprocessed_dataset.csv")

# Create target labels
def create_risk(value):
    if value > 1:
        return "High"
    elif value > 0:
        return "Medium"
    else:
        return "Low"

df["Risk_Label"] = df["Total Affected"].apply(create_risk)

# Encode target
label_encoder = LabelEncoder()
df["Risk_Label"] = label_encoder.fit_transform(df["Risk_Label"])

# Select only numeric features
X = df.drop(["Risk_Label"], axis=1, errors="ignore")
X = X.select_dtypes(include=["number"])

y = df["Risk_Label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))