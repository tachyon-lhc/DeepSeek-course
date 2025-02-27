"""
Ejercicio 1: Escalado y Codificación
    Objetivo:
            Dado un DataFrame que contenga variables numéricas y categóricas
            (por ejemplo, "edad", "ingresos" y "género"), crea una transformación que:

                  - Escale las variables numéricas con MinMaxScaler.
                  - Codifique la variable "género" usando OneHotEncoder.

    Tarea:
            Usa ColumnTransformer y un Pipeline para realizar la transformación
            y muestra el resultado transformado.
"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

df_pipeline = pd.DataFrame(
    {
        "edad": [23, 51, 67, 19, 32, 54],
        "ingresos": [4000, 1000, 1200, 7000, 12000, 3000],
        "genero": [
            "masculino",
            "masculino",
            "femenino",
            "masculino",
            "femenino",
            "masculino",
        ],
    }
)

print(df_pipeline)
print()

num_cols = ["edad", "ingresos"]
cat_cols = ["genero"]

ct = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(), cat_cols),
    ]
)

pipeline = Pipeline(steps=[("preprocessor", ct)])

df_transformed = pd.DataFrame(
    pipeline.fit_transform(df_pipeline),
    columns=pd.Index(
        [
            *num_cols,
            *pipeline.named_steps["preprocessor"]
            .transformers_[1][1]
            .get_feature_names_out(cat_cols),
        ]
    ),
)
print(df_transformed)
