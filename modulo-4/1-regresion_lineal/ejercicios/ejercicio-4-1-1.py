from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_california_housing
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

"""
Comparacion entre el modelo lineal y el modelo RandomForest
"""

# cargar dataset
california = fetch_california_housing(as_frame=True)
df = california.frame

# variables categoricas y numericas
num_cols = list(df.columns.difference(["MedHouseVal"]))

# Modelos
modelo_1 = LinearRegression()
modelo_2 = RandomForestRegressor()


# Pipeline para cada tipo de columna

num_pipeline = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="mean")), ("scaler", StandardScaler())]
)

# Aplicar procesos a las clumnas
prepoccesor = ColumnTransformer(transformers=[("num", num_pipeline, num_cols)])

# Definir X (características) e y (variable objetivo)
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# Entrenamiento y testeo

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline completo para ambos modelos
pipeline_lineal = Pipeline(
    steps=[("prepoccesor", prepoccesor), ("regressor", modelo_1)]
)

pipeline_RandomForest = Pipeline(
    steps=[("prepoccesor", prepoccesor), ("regressor", modelo_2)]
)

# Entrenarmiento de los modelos
pipeline_lineal.fit(X_train, y_train)
pipeline_RandomForest.fit(X_train, y_train)

# Calcular prediccioens
y_pred_lineal = pipeline_lineal.predict(X_test)
y_pred_RandomForest = pipeline_RandomForest.predict(X_test)

# Calcular metricas
mse_lineal = mean_squared_error(y_test, y_pred_lineal)
r2_lineal = r2_score(y_test, y_pred_lineal)

mse_RandomForest = mean_squared_error(y_test, y_pred_RandomForest)
r2_RandomForest = r2_score(y_test, y_pred_RandomForest)

# Resultados
print(f"Modelo Lineal - MSE: {mse_lineal:.2f}, R²: {r2_lineal:.2f}")
print(f"Modelo RandomForest - MSE: {mse_RandomForest:.2f}, R²: {r2_RandomForest:.2f}")
