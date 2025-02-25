"""
 Ejemplo Práctico: Clasificación de Especies de Flores (Iris)
Dataset: Usaremos el dataset Iris, que contiene datos de cuatro características de flores y clasifican en tres especies.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# Cargar dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Inicializar y entrenar el modelo
modelo = DecisionTreeClassifier(criterion="gini", max_depth=3)
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_test)

print(f"Exactitud: {accuracy_score(y_test, y_pred):.2f}")
print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=target_names))

plt.figure(figsize=(12, 8))
plot_tree(modelo, feature_names=feature_names, class_names=target_names, filled=True)
plt.show()
