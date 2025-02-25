from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
import matplotlib.pyplot as plt

# Cargar dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Divinir en entrenamiento y pruebas
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Escalar datos de entrada
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# Entrar el modelo
modelo = LogisticRegression()
modelo.fit(X_train_scaled, y_train)

# Predicciones
y_pred = modelo.predict(X_test_scaled)
y_prob = modelo.predict_proba(X_test_scaled)[:, 1]

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)
print(f"Accuracy: {accuracy:.2f}")
print(f"ROC-AUC: {roc_auc:.2f}")

# Reporte detallado
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Coeficientes del modelo
coef = modelo.coef_[0]
features = data.feature_names

# Visualizar coeficientes
plt.figure(figsize=(10, 6))
plt.bar(features, coef)
plt.xticks(rotation=90)
plt.title("Coeficientes de la Regresión Logística")
plt.ylabel("Coeficiente")
plt.show()
