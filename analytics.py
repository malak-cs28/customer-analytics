import sys
import pandas as pd
import subprocess

# Get preprocessed CSV path from command line
file_path = sys.argv[1]
df = pd.read_csv(file_path)

# Insight 1: Most trips by time period
time_counts = df['time_period'].value_counts()
top_period = time_counts.idxmax()
top_count = time_counts.max()
insight1 = f"Most Uber trips happen during {top_period} ({top_count} trips)."

with open('insight1.txt', 'w') as f:
    f.write(insight1)

# Insight 2: Most active Base
base_counts = df['Base'].value_counts()
top_base = base_counts.idxmax()
top_base_count = base_counts.max()
insight2 = f"The most active Base is {top_base} with {top_base_count} trips."

with open('insight2.txt', 'w') as f:
    f.write(insight2)

# Insight 3: Most active weekday
weekday_counts = df['weekday'].value_counts()
top_weekday = weekday_counts.idxmax()
top_weekday_count = weekday_counts.max()
insight3 = f"The busiest weekday is {top_weekday} with {top_weekday_count} trips."

with open('insight3.txt', 'w') as f:
    f.write(insight3)

print("Analytics complete! Saved insight1.txt, insight2.txt, and insight3.txt.")

# Call visualize.py
subprocess.run(["python", "visualize.py", file_path])