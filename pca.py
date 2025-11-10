# 1. Import required libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 2. Load Dataset
iris = load_iris()
X = iris.data               # features
y = iris.target             # labels
target_names = iris.target_names

# 3. Standardize Data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Apply PCA (reduce to 2 components)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 5. Plot Before PCA (Using first two original features)
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
for i, target in enumerate(np.unique(y)):
    plt.scatter(X[y==target, 0], X[y==target, 1], label=target_names[target])
plt.title('Before PCA (Original Features)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()

# 6. Plot After PCA
plt.subplot(1,2,2)
for i, target in enumerate(np.unique(y)):
    plt.scatter(X_pca[y==target, 0], X_pca[y==target, 1], label=target_names[target])
plt.title('After PCA (PC1 vs PC2)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()

plt.show()

# 7. Print explained variance ratio (how much info retained)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Total variance preserved:", sum(pca.explained_variance_ratio_))
