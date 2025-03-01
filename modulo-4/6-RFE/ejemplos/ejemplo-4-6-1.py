from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
import numpy as np

# Cargar dataset
diabetes = fetch_openml(name="diabetes", version=1, as_frame=True)
X = diabetes.data
y = diabetes.target  # 'tested_negative' or 'tested_positive'

# Convertir target a binario
y = np.where(y == "tested_positive", 1, 0).astype(int)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Escalar variables numéricas
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicializar modelo base (Logistic Regression)
modelo_base = LogisticRegression(solver="liblinear")

# Inicializar RFE
rfe = RFE(estimator=modelo_base, n_features_to_select=4)
X_train_selected = rfe.fit_transform(X_train_scaled, y_train)
X_test_selected = rfe.transform(X_test_scaled)

# Entrenar Gradient Boosting con features seleccionados
modelo = GradientBoostingClassifier(
    n_estimators=150, learning_rate=0.05, max_depth=3, subsample=0.8, random_state=42
)
modelo.fit(X_train_selected, y_train)

# Predecir
y_pred = modelo.predict(X_test_selected)

print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))
