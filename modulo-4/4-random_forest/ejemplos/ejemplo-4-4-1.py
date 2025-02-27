from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
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
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_test)

print(f"Exactitud: {accuracy_score(y_test, y_pred):.2f}")
print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Calcula la importancia de las características
importances = modelo.feature_importances_

# Grafica la importancia de las características
plt.figure(figsize=(10, 5))
plt.bar(feature_names, importances)
plt.title("Importancia de Características - Bosque Aleatorio")
plt.ylabel("Importancia")
plt.xticks(rotation=45)
plt.show()
