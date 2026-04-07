import pandas as pd

file_path = "C:/AI_Disaster_Project/data/disaster_history.xlsx"

df = pd.read_excel(file_path)

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)