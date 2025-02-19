import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# cargar el datasets
california = fetch_california_housing(as_frame=True)
df = california.frame

# Crear una variable categórica 'region' a partir de 'Latitude'
median_lat = df["Latitude"].median()
df["region"] = np.where(df["Latitude"] > median_lat, "Norte", "Sur")

# Definir columnas numéricas y categóricas
num_cols = list(
    df.columns.difference(["region", "MedHouseVal"])
)  # Excluimos la variable categórica y la target
cat_cols = ["region"]

# Crear pipelines para cada tipo de columna
num_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="mean"),
        ),  # Aunque no haya faltantes, se incluye como ejemplo
        ("scaler", StandardScaler()),
    ]
)

cat_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent"),
        ),  # Para imputar si hay faltantes en categorías
        ("onehot", OneHotEncoder()),
    ]
)

# ColumnTransformer que aplica cada pipeline a las columnas correspondientes
preprocessor = ColumnTransformer(
    transformers=[("num", num_pipeline, num_cols), ("cat", cat_pipeline, cat_cols)]
)

# Definir X (características) e y (variable objetivo)
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# División en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline completo: preprocesamiento + modelo de regresión lineal
pipelineLinear = Pipeline(
    steps=[("preprocessor", preprocessor), ("regressor", LinearRegression())]
)

pipelineRandomForest = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
    ]
)

# entranando los modelos
pipelineLinear.fit(X_train, y_train)
pipelineRandomForest.fit(X_train, y_train)

# Predicciones en el conjunto de prueba
y_predLinear = pipelineLinear.predict(X_test)
y_predRandomForest = pipelineRandomForest.predict(X_test)

# Calcular MSE y R2
mseL = mean_squared_error(y_test, y_predLinear)
r2L = r2_score(y_test, y_predLinear)

mseRF = mean_squared_error(y_test, y_predRandomForest)
r2RF = r2_score(y_test, y_predRandomForest)

print("Evaluación del Modelo Lineal:")
print(f"MSE: {mseL:.2f}")
print(f"R^2: {r2L:.2f}")

print()

print("evaluacion del modulo Random Forest: ")
print(f"MSE: {mseRF:.2f}")
print(f"R^2: {r2RF:.2f}")
