# Ejemplo 1: Escalado de Características
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Datos de ejemplo
df = pd.DataFrame({"altura": [150, 160, 170, 180, 190], "peso": [50, 60, 70, 80, 90]})

# Escalado con StandardScaler
scaler_std = StandardScaler()
df_std = pd.DataFrame(scaler_std.fit_transform(df), columns=df.columns)
print("StandardScaler:")
print(df_std)

# Escalado con MinMaxScaler
scaler_minmax = MinMaxScaler()
df_minmax = pd.DataFrame(scaler_minmax.fit_transform(df), columns=df.columns)
print("\nMinMaxScaler:")
print(df_minmax)
