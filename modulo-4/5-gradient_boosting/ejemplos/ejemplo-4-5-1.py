from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Cargar dataset
iris = load_iris()
X, y = iris.data, iris.target

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar Gradient Boosting
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
gb_model.fit(X_train, y_train)
y_pred_gb = gb_model.predict(X_test)

# Entrenar Random Forest
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Resultados
print("Gradient Boosting (Exactitud):", accuracy_score(y_test, y_pred_gb))
print("Random Forest (Exactitud):", accuracy_score(y_test, y_pred_rf))

# Reporte de clasificación para Gradient Boosting
print("\nReporte de Gradient Boosting:")
print(classification_report(y_test, y_pred_gb, target_names=iris.target_names))
