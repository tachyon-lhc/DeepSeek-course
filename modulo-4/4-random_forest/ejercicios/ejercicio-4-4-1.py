from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Cargar dataset
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
feature_names = cancer.feature_names
target_names = cancer.target_names

# Dividir en entrenamiento y testeo
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Escalar datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# Entrenar modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train_scaled, y_train)

# Prediccion
y_pred = modelo.predict(X_test_scaled)
print(f"Exactitud: {accuracy_score(y_test, y_pred):.2f}")
print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Graficar datos importantes
importances = modelo.feature_importances_
plt.figure(figsize=(17, 7))
plt.bar(feature_names, importances)
plt.title("Importancia de Características - Bosque Aleatorio")
plt.ylabel("Importancia")
plt.xticks(rotation=90, fontsize=10)
plt.tight_layout()
plt.show()
