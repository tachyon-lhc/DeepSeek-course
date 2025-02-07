# Ejemplo 2: Subplots en Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2, 1, figsize=(8, 8))  # 2 filas, 1 columna
axs[0].plot(x, y1, color='red')
axs[0].set_title('Seno')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Seno')

axs[1].plot(x, y2, color='green')
axs[1].set_title('Coseno')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Coseno')

plt.tight_layout()

plt.savefig('./tmp/subplot.png')
