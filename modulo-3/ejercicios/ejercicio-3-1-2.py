import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

"""
Ejercicio Propuesto:
Genera un DataFrame:
Crea un DataFrame con 300 muestras y 8 variables numéricas. Puedes usar np.random.rand para generar los datos.

Aplica t-SNE:

Utiliza t-SNE para reducir la dimensionalidad a 2 componentes.
Asegúrate de fijar una semilla aleatoria (por ejemplo, random_state=42) para reproducibilidad.
Visualiza el Resultado:
"""

np.random.seed(42)
data = np.random.rand(300, 8)

df = pd.DataFrame(data, columns=pd.Index([f"Index_{i}" for i in range(1, 9)]))

tsne_data = TSNE(n_components=2, random_state=42)
tsne_results = tsne_data.fit_transform(df)

df_tsne = pd.DataFrame(tsne_results, columns=pd.Index(["Dim-1", "Dim-2"]))

plt.figure(figsize=(8, 6))
plt.title("t-SNE")
plt.scatter(df_tsne["Dim-1"], df_tsne["Dim-2"], c="red", alpha=0.6)
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.savefig("./tmp/tsne.png")

plt.show()
