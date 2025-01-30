import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler

# Generate synthetic dataset (moons, non-linearly separable clusters)
X, _ = make_moons(n_samples=500, noise=0.05, random_state=42)
X = StandardScaler().fit_transform(X)  # Normalize for better DBSCAN performance

# Apply K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# K-Means plot
axes[0].scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', s=20, edgecolors='k')
axes[0].set_title("K-Means Clustering")

# DBSCAN plot
axes[1].scatter(X[:, 0], X[:, 1], c=dbscan_labels, cmap='viridis', s=20, edgecolors='k')
axes[1].set_title("DBSCAN Clustering (Noise in -1)")

plt.show()

# Count unique clusters (DBSCAN detects noise as -1)
num_kmeans_clusters = len(set(kmeans_labels))
num_dbscan_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
num_noise_points = list(dbscan_labels).count(-1)

num_kmeans_clusters, num_dbscan_clusters, num_noise_points
