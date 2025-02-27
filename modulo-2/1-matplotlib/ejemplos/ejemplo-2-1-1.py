import matplotlib.pyplot as plt
import numpy as np

# Ejemplo 1: Gráfico Simple con Matplotlib
# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear figura y eje
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Seno', color='blue', linewidth=2)
plt.title('Gráfico de la función Seno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.annotate('Máximo', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 0.8),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Guardar la figura en un archivo
plt.savefig('./tmp/grafico_seno.png')
