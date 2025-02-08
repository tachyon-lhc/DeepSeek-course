# Ejemplo 3: Boxplot para Comparar Distribuciones entre Categorías
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
df_box = pd.DataFrame({
    'Ventas': np.concatenate([np.random.normal(100, 15, 100),
                               np.random.normal(120, 20, 100),
                               np.random.normal(80, 10, 100)]),
    'Producto': ['Producto A']*100 + ['Producto B']*100 + ['Producto C']*100
})

# Crear un boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Producto', y='Ventas', data=df_box, palette='Set2', legend=False, hue='Producto')
plt.title('Distribución de Ventas por Producto')
plt.savefig('./tmp/boxplot.png')
print(df_box)
