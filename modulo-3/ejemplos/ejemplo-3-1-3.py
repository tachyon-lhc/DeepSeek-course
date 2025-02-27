# Ejemplo 3: Reducción de Dimensionalidad con PCA
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

# Generar un DataFrame de ejemplo con 4 variables
np.random.seed(42)
df_pca = pd.DataFrame(np.random.rand(100, 4), columns=pd.Index(["A", "B", "C", "D"]))

# Aplicar PCA para reducir a 2 componentes
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_pca)
df_pca_reducido = pd.DataFrame(pca_result, columns=pd.Index(["PC1", "PC2"]))
print("Resultado de PCA (2 componentes):")
print(df_pca_reducido.head(20))
