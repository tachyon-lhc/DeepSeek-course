import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargar dataset
data = fetch_california_housing()

print(data.feature_names)

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Crear nuevas características antes de dividir
median_lat = X["Latitude"].median()
X["region"] = np.where(
    X["Latitude"] > median_lat, "Norte", "Sur"
)  # Variable categórica
X["total_rooms"] = X["AveRooms"] + X["AveBedrms"]
X["rooms_per_household"] = X["total_rooms"] / X["AveOccup"]
X["population_per_household"] = X["Population"] / X["AveOccup"]

print(X.head())

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo 1: Sin nuevas características
modelo = LinearRegression()
modelo.fit(
    X_train.drop(columns=["region"]), y_train
)  # Excluimos "region" porque es categórica
y_pred = modelo.predict(X_test.drop(columns=["region"]))
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Modelo 1 - MSE: {mse:.2f}, R²: {r2:.2f}")

# Modelo 2: Con nuevas características y "region" codificada
# Codificar "region" (One-Hot Encoding)
X_train_encoded = pd.get_dummies(X_train, columns=["region"], drop_first=True)
X_test_encoded = pd.get_dummies(X_test, columns=["region"], drop_first=True)

modelo2 = LinearRegression()
modelo2.fit(X_train_encoded, y_train)
y_pred2 = modelo2.predict(X_test_encoded)
mse2 = mean_squared_error(y_test, y_pred2)
r22 = r2_score(y_test, y_pred2)
print(f"Modelo 2 - MSE: {mse2:.2f}, R²: {r22:.2f}")
