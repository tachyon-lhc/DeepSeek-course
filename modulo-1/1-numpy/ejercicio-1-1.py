import numpy as np

'''
Ejercicio 1: Crear un Array y Realizar Operaciones:
        Crea un array de 10 elementos con valores del 0 al 9.
        Multiplica cada elemento por 3 y resta 5.
'''
array_1 = np.arange(10)
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
secondRow = matrix_1[1, :]
thridColumn = matrix_1[:, 2]
subMatrix = matrix_1[:2, :2]

'''
Ejercicio 3: Álgebra Lineal
    Dadas las siguientes matrices:

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    - Calcula el producto de las matrices A y B.

    - Calcula la transpuesta de la matriz A.
'''
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
productMatrix = A @ B

def main():
    print(f"De la lista{array_1} cada elemento * 3 -5: {operation_1}\n")
    print(matrix_1)
    # segunda fila
    print(f"Segunda fila: {secondRow}")
    # tercera columna
    print(f"Tercera columna: {thridColumn}")
    # dos primeras filas, dos ultimas columnas
    print(f"Submatriz: \n{subMatrix}\n")
    print(f"{A}\n * \n{B}\n = \n{productMatrix}")

if __name__ == '__main__':
    main()
