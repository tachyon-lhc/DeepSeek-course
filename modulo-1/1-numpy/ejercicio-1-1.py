import numpy as np

'''
Ejercicio 1: Crear un Array y Realizar Operaciones:
        Crea un array de 10 elementos con valores del 0 al 9.
        Multiplica cada elemento por 3 y resta 5.
'''
array_1 = np.array([i for i in range(10)])
operation_1 = (array_1*3 -5)


'''
Ejercicio 2: Indexación y Slicing:
    Dado el siguiente array:
                            array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    - Extrae la segunda fila.

    - Extrae la tercera columna.

    - Extrae la submatriz de las dos primeras filas y las dos primeras columnas.
'''
matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix_1)
# segunda fila
print(f"Segunda fila: {matrix_1[1, :]}")
# tercera columna
print(f"Tercera columna: {matrix_1[:, 2]}")
# dos primeras filas, dos ultimas columnas
print(f"Submatriz: \n{matrix_1[:2, :2]}")

'''

'''
