# Ejemplo 2: Pairplot para Visualizar Relaciones entre Variables
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo con variables numéricas y una categórica
df_pair = pd.DataFrame({
    'Longitud': np.random.normal(5, 2, 100),
    'Anchura': np.random.normal(3, 1, 100),
    'Altura': np.random.normal(10, 3, 100),
    'Categoría': np.random.choice(['Tipo A', 'Tipo B'], 100)
})

# Crear un pairplot diferenciando por la categoría
sns.pairplot(df_pair, hue='Categoría', diag_kind='kde')
plt.suptitle('Pairplot de Variables', y=1.02)
plt.savefig('./tmp/pairplot.png')
print(df_pair)
