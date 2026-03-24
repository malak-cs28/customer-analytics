import sys
import pandas as pd
import subprocess

# Step 1: Get input file path from command line
file_path = sys.argv[1]

# Step 2: Load the dataset
try:
    df = pd.read_csv(file_path)
    print(f"Preprocessing started. Original shape: {df.shape}")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: File '{file_path}' is empty.")
    sys.exit(1)

# 1) Data Cleaning

# Remove missing values
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date/Time to datetime format
df["Date/Time"] = pd.to_datetime(df["Date/Time"], errors="coerce")

# Remove rows where Date/Time conversion failed
df = df.dropna(subset=["Date/Time"])

# Remove invalid latitude and longitude values
df = df[(df["Lat"].between(-90, 90)) & (df["Lon"].between(-180, 180))]
print(f"After cleaning: {df.shape}")

# 2) Feature Transformation

# Extract hour, day, and weekday
df["hour"] = df["Date/Time"].dt.hour
df["day"] = df["Date/Time"].dt.day
df["weekday"] = df["Date/Time"].dt.day_name()

# Encode Base column manually using category codes
df["Base_encoded"] = df["Base"].astype("category").cat.codes

#Scaling numerical features using Min-Max Scaling
def min_max_scale(series):
    if series.max() == series.min():
        return 0
    return (series - series.min()) / (series.max() - series.min())
df["Lat_scaled"] = min_max_scale(df["Lat"])
df["Lon_scaled"] = min_max_scale(df["Lon"])
df["hour_scaled"] = min_max_scale(df["hour"])
df["day_scaled"] = min_max_scale(df["day"])
df["Base_encoded_scaled"] = min_max_scale(df["Base_encoded"])

# 3) Discretization
def get_time_period(hour):
    if 0 <= hour <= 5:
        return "Night"
    elif 6 <= hour <= 11:
        return "Morning"
    elif 12 <= hour <= 17:
        return "Afternoon"
    else:
        return "Evening"

df["time_period"] = df["hour"].apply(get_time_period)

# 4) Dimensionality Reduction
selected_columns = [
    "Date/Time",
    "Lat",
    "Lon",
    "Base",
    "hour",
    "day",
    "weekday",
    "Base_encoded",
    "time_period",
    "Lat_scaled",
    "Lon_scaled",
    "hour_scaled",
    "day_scaled",
    "Base_encoded_scaled"
]
df = df[selected_columns]
print(f"After preprocessing and feature selection: {df.shape}")

# Step 3: Save preprocessed data
df.to_csv("data_preprocessed.csv", index=False)
print("Saved data_preprocessed.csv successfully.")



# Step 4: call analytics.py automatically
subprocess.run(
        ["python", "analytics.py", "data_preprocessed.csv"],
        check=True
    )
