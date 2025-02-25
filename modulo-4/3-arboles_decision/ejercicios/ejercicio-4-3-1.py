import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt


file_path = "~/workspace/deepseek-python/DeepSeek-course/modulo-4/datasets/WineQT.csv"
df = pd.read_csv(file_path)

X = df.drop(columns=["Id", "quality"])
y = df["quality"]

feature_names = X.columns
labels = np.unique(y)
target_names = [str(label) for label in labels]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar al modelo
modelo = DecisionTreeClassifier(
    criterion="gini", max_depth=4, min_samples_split=20, random_state=42
)
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_test)
print(f"Exactitud: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred, labels=labels, target_names=target_names))

plt.figure(figsize=(12, 8))
plot_tree(modelo, feature_names=feature_names, class_names=target_names, filled=True)
plt.show()
