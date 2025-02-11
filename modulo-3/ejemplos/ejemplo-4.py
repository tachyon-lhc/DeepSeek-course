# Ejemplo 4: Uso de Pipelines con ColumnTransformer
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

# Crear DataFrame de ejemplo
df_pipeline = pd.DataFrame(
    {
        "edad": [25, 32, 47, 51, 38],
        "salario": [50000, 60000, 80000, 90000, 75000],
        "departamento": ["ventas", "marketing", "ventas", "finanzas", "marketing"],
    }
)
print(df_pipeline)

# Definir las columnas numéricas y categóricas
num_cols = ["edad", "salario"]
cat_cols = ["departamento"]

# Crear ColumnTransformer
ct = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(), cat_cols),
    ]
)

# Crear Pipeline (por ejemplo, solo la transformación)
pipeline = Pipeline(steps=[("preprocessor", ct)])

# Aplicar la transformación
df_transformed = pipeline.fit_transform(df_pipeline)
print("Resultado de la transformación con Pipeline:")
print(df_transformed)
