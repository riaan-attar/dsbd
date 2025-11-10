# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

# Step 2: Load Dataset (iris.csv should be in the same folder)
data = pd.read_csv("iris.csv")

# Step 3: Separate features and labels
X = data.iloc[:, :-1]   # All columns except last (sepal/petal data)
y = data.iloc[:, -1]    # Last column (species)

# Step 4: Split Dataset into Train and Test (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Step 5: Create KNN Model (k = 3)
knn = KNeighborsClassifier(n_neighbors=3)

# Step 6: Train the Model
knn.fit(X_train, y_train)

# Step 7: Predict
y_pred = knn.predict(X_test)

# Step 8: Compute Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)
