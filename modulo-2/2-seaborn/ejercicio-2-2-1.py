# 09/02/2025
'''
Ejercicio 1: Crear un Heatmap de Correlación
    Objetivo:
             Dado un DataFrame (puedes generar uno con datos aleatorios
             o utilizar uno real), calcula la matriz de correlación entre
             sus variables y crea un heatmap.
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.rand(10, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

corr_matrix = df.corr()

# Crear un heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='rocket')
plt.tittle('Matrix de correlacion')

print(data)
print()
print(df)
print()
