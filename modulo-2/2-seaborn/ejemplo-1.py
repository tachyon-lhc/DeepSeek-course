# Ejemplo 1: Heatmap de una Matriz de Correlación
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = np.random.rand(10, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

# Calcular la matriz de correlación
corr_matrix = df.corr()

# Crear un heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='rocket')
plt.title('Heatmap de la Matriz de Correlación')
plt.savefig('./tmp/heatmap.png')
print(df)
