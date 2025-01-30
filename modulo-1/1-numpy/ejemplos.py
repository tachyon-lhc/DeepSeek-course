import numpy as np

# Ejemplo 1: Crear un Array a partir de una lista
array = np.array([1, 2, 3, 4, 5])
print(array)  # Output: [1 2 3 4 5]

# Ejemplo 2: Operaciones Vectorizadas
array = np.array([1, 2, 3, 4, 5])
print(array + 10)  # Output: [11 12 13 14 15]
print(array * 2)   # Output: [2 4 6 8 10]

# Ejemplo 3: Indexación y Slicing
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array[0, 1])  # Output: 2 (fila 0, columna 1)
print(array[:, 1])  # Output: [2 5 8] (toda la columna 1)

# Ejemplo 4: Álgebra Lineal: Producto de matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
producto = np.dot(A, B)
print(producto)  # Output: [[19 22] [43 50]]
