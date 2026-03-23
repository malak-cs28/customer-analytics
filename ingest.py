import sys
import pandas as pd
import subprocess

# Step 1: Get dataset path from command line
file_path = sys.argv[1]

# Step 2: Load the dataset
try:
    df = pd.read_csv(file_path)
    print(f"Dataset loaded successfully! Shape: {df.shape}")
    print("Columns:", df.columns.tolist())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: File '{file_path}' is empty.")
    sys.exit(1)

# Step 3: Save a copy as data_raw.csv
df.to_csv("data_raw.csv", index=False)
print("Saved data_raw.csv successfully.")

# Step 4: call to preprocess.py 
subprocess.run(["python", "preprocess.py", "data_raw.csv"])