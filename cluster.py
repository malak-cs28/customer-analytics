import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Get preprocessed CSV path from command line
file_path = sys.argv[1]
df = pd.read_csv(file_path)

# Select features for clustering
X = df[['Lat', 'Lon', 'hour']]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Count samples in each cluster
cluster_counts = df['Cluster'].value_counts().sort_index()

# Save results to clusters.txt
with open('clusters.txt', 'w') as f:
    for cluster_id, count in cluster_counts.items():
        f.write(f"Cluster {cluster_id}: {count} samples\n")

print("Clustering complete! Saved clusters.txt.")