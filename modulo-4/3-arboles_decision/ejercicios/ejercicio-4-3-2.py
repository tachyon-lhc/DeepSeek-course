import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report

# Cargar el dataset
file_path = "~/workspace/deepseek-python/DeepSeek-course/modulo-4/datasets/fraud.csv"
df = pd.read_csv(file_path)

# Dividir en features y target
X = df.drop(columns=["Transaction_ID", "Fraud_Label"])
y = df["Fraud_Label"]

# Dividir en entrenamiento y testeo
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Identificar variables categóricas en el conjunto de entrenamiento
categorical_cols = X_train.select_dtypes(include=["object"]).columns

# Preprocesar con ColumnTransformer para codificación de variables categóricas
preprocessor = ColumnTransformer(
    transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)],
    remainder="passthrough",  # Conserva las variables numéricas
)

# Aplica el preprocesamiento a datos de entrenamiento y prueba
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Entrenar el modelo
modelo = DecisionTreeClassifier(criterion="gini", max_depth=3)
modelo.fit(X_train_processed, y_train)

# Predecir
y_pred = modelo.predict(X_test_processed)

# Evaluar
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Exactitud: {accuracy:.2f}")
print("Reporte de Clasificación:")
print(report)
