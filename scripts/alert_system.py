import pandas as pd

df = pd.read_csv("C:/AI_Disaster_Project/data/predictions.csv")

high_risk = df[df["Severity"] == "High"]

print("🚨 ACTIVE ALERTS")
print("-" * 40)

for _, row in high_risk.iterrows():
    print(
        f"⚠ ALERT: {row['Disaster_Type']} HIGH risk in "
        f"{row['Region']} | Probability: {row['Probability']}"
    )