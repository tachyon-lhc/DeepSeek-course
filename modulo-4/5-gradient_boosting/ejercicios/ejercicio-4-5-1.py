from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load dataset
diabetes = fetch_openml(name="diabetes", version=1, as_frame=True)
X = diabetes.data
y = diabetes.target  # 'tested_negative' or 'tested_positive'

# Convert target to binary
y = np.where(y == "tested_positive", 1, 0).astype(int)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Preprocess numerical features with StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Gradient Boosting Classifier with class balancing
modelo = GradientBoostingClassifier(
    n_estimators=150,
    learning_rate=0.05,
    max_depth=3,
    subsample=0.8,
    random_state=42,
)
modelo.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = modelo.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Gradient Boosting Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))
