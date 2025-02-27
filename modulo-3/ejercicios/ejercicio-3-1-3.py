import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Crear un DataFrame de ejemplo con valores faltantes
df = pd.DataFrame(
    {
        "edad": [19, None, 22, 91, 32, 54],
        "ingresos": [4000, 1000, None, 7000, 12000, 3000],
        "genero": ["masculino", "masculino", "femenino", None, "femenino", "masculino"],
    }
)

print(f"df original:\n{df}")

num_cols = ["edad", "ingresos"]
cat_cols = ["genero"]

# pipeline para rellenar datos None

num_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="mean"),
        ),
        ("scaler", StandardScaler()),
    ]
)

cat_pipeline = Pipeline(
    steps=[
        ("impuer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder()),
    ]
)

# aplicar pipeline a las columnas
preprocessor = ColumnTransformer(
    transformers=[("num", num_pipeline, num_cols), ("cat", cat_pipeline, cat_cols)]
)

# pipeline completo
pipeline = Pipeline(steps=[("preprocessor", preprocessor)])

# aplicarlo al df
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

print(f"\n{df_transformed}")
