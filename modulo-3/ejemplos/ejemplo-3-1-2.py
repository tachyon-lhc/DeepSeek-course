# Ejemplo 2: Codificación de Variables Categóricas
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Datos de ejemplo
df_cat = pd.DataFrame({"color": ["rojo", "azul", "verde", "azul", "rojo"]})

# Usando LabelEncoder
le = LabelEncoder()
df_cat["color_label"] = le.fit_transform(df_cat["color"])
print("LabelEncoder:")
print(df_cat)

# Usando OneHotEncoder (conversión a array y luego a DataFrame)
ohe = OneHotEncoder(sparse_output=False)
color_encoded = ohe.fit_transform(df_cat[["color"]])
df_ohe = pd.DataFrame(color_encoded, columns=ohe.get_feature_names_out(["color"]))
print("\nOneHotEncoder:")
print(df_ohe)
