import numpy as np
import matplotlib.pyplot as plt

'''
Crear un gráfico de dispersión (scatter plot) que muestre 50 puntos aleatorios,
personalizando el gráfico con título, etiquetas, colores, tamaño de los puntos
y una línea de tendencia.
'''

np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)

# Crear un scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', s=50, alpha=0.7, label='Caos')

# personalizando el grafico
plt.title('Grafico de dispersion con linea de tendecnia')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Calcular y graficar la linea de tendencia
# Ajuste lineal: y = mx + b
m, b = np.polyfit(x, y, 1)

# Generar valores para la linea de tendencia
x_fit = np.linspace(0, 1, 100)
y_fit = m*x_fit + b
plt.plot(x_fit, y_fit, color='blue', linewidth=2,
         label=f'Linea de tendencia\n(y={m:.2f}x+{b:.2f})')

plt.legend()

plt.savefig('./tmp/grafico_dispersion.png')
