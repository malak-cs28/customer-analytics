import sys
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

# Get preprocessed CSV path from command line
file_path = sys.argv[1]
df = pd.read_csv(file_path)

# Create one figure with 3 plots
plt.figure(figsize=(18, 5))

# Plot 1: Trips by time period
plt.subplot(1, 3, 1)
time_counts = df['time_period'].value_counts()
plt.bar(time_counts.index, time_counts.values)
plt.title('Trips by Time Period')
plt.xlabel('Time Period')
plt.ylabel('Number of Trips')

# Plot 2: Trips by Base
plt.subplot(1, 3, 2)
base_counts = df['Base'].value_counts()
plt.bar(base_counts.index, base_counts.values)
plt.title('Trips by Base')
plt.xlabel('Base')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)

# Plot 3: Pickup locations
plt.subplot(1, 3, 3)
plt.scatter(df['Lon'], df['Lat'], s=1)
plt.title('Pickup Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save the figure
plt.tight_layout()
plt.savefig('summary_plot.png')

print("Visualization complete! Saved summary_plot.png.")


# Call cluster.py
try:
	subprocess.run(["python", "cluster.py", file_path], check=True)
	print("cluster.py ran successfully!")
except subprocess.CalledProcessError:
	print("Error: cluster.py failed to run.")
	sys.exit(1)