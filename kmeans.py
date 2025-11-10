# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 2: Load Dataset
iris = load_iris()
X = iris.data   # Only numeric features

# Step 3: Standardize the Data (important for clustering)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Elbow Method to Find Optimal k
wcss = []  # Within-Cluster-Sum-of-Squares

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)  # inertia = WCSS

# Step 5: Plot Elbow Graph
plt.figure(figsize=(7,5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method to Determine Optimal Number of Clusters")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS (Inertia)")
plt.show()

# Step 6: Choose optimal k (from elbow) and apply K-Means
k_optimal = 3  # From elbow plot (for Iris it is usually 3)
kmeans = KMeans(n_clusters=k_optimal, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Step 7: Add cluster info to a DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["Cluster"] = clusters

print(df.head())
