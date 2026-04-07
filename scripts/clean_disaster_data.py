import pandas as pd

# Read Excel file
file_path = "C:/AI_Disaster_Project/data/disaster_history.xlsx"
df = pd.read_excel(file_path)

# Select important columns
selected_columns = [
    "Country",
    "Location",
    "Disaster Type",
    "Latitude",
    "Longitude",
    "Start Year",
    "Total Deaths",
    "Total Affected"
]

clean_df = df[selected_columns]

# Remove missing values
clean_df = clean_df.dropna()

# Save cleaned CSV
clean_df.to_csv("C:/AI_Disaster_Project/data/clean_disaster_data.csv", index=False)

print("Cleaned Data:")
print(clean_df.head())

print("\nRows and Columns:")
print(clean_df.shape)