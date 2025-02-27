import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Generar datos de ejemplo: 200 muestras con 5 características
np.random.seed(42)
data = np.random.rand(200, 5)
df_data = pd.DataFrame(data, columns=pd.Index([f"feature_{i}" for i in range(1, 6)]))

# Aplicar t-SNE para reducir a 2 dimensiones
tsne = TSNE(n_components=2, random_state=42)
tsne_result = tsne.fit_transform(df_data)

# Crear un DataFrame con los resultados
df_tsne = pd.DataFrame(tsne_result, columns=pd.Index(["Dim1", "Dim2"]))

# Graficar el resultado
plt.figure(figsize=(8, 6))
plt.scatter(df_tsne["Dim1"], df_tsne["Dim2"], c="blue", alpha=0.6)
plt.title("Visualización de Datos con t-SNE")
plt.xlabel("Dimensión 1")
plt.ylabel("Dimensión 2")
plt.savefig("./tmp/tsne.png")
