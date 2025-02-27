import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Crear un DataFrame de ejemplo con valores faltantes
df = pd.DataFrame(
    {
        "edad": [23, None, 67, 19, 32, 54],
        "ingresos": [4000, 1000, None, 7000, 12000, 3000],
        "genero": ["masculino", "masculino", "femenino", None, "femenino", "masculino"],
    }
)

print("DataFrame Original:")
print(df)
print()

# Definir columnas numéricas y categóricas
num_cols = ["edad", "ingresos"]
cat_cols = ["genero"]

# Pipeline para variables numéricas:
num_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="mean"),
        ),  # Imputa valores faltantes con la media
        ("scaler", StandardScaler()),  # Escala los datos
    ]
)

# Pipeline para variables categóricas:
cat_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),  # Imputa con la moda
        ("onehot", OneHotEncoder()),  # Codifica en variables dummy
    ]
)

# ColumnTransformer para aplicar cada pipeline a sus columnas correspondientes
preprocessor = ColumnTransformer(
    transformers=[("num", num_pipeline, num_cols), ("cat", cat_pipeline, cat_cols)]
)

# Crear el pipeline completo
pipeline = Pipeline(steps=[("preprocessor", preprocessor)])

# Aplicar el pipeline al DataFrame
df_transformed = pd.DataFrame(
    pipeline.fit_transform(df),
    columns=pd.Index(
        [
            *num_cols,
            *pipeline.named_steps["preprocessor"]
            .named_transformers_["cat"]
            .named_steps["onehot"]
            .get_feature_names_out(cat_cols),
        ]
    ),
)

print("Resultado Transformado:")
print(df_transformed)
