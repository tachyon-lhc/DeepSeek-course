# Crea una lista con los cubos de los números del 1 al 5 usando list comprehension.
cubos = [x**3 for x in range(1,6)]

# Crear un diccionario que mapee cada número del 1 al 5 a su cuadrado.
alfabeto = {x: chr(x + 96) for x in range(1, 27)}

# Crea un conjunto con los números impares del 1 al 15 usando set comprehension.
impares = {x for x in range(1,16) if x % 2 != 0}

# Crea una lista de tuplas, donde cada tupla contenga un número y su cubo, solo para números impares del 1 al 10
cubosImpares = [(x, x**3) for x in range(1,11) if x % 2 != 0]

def main():
    print(f'\nCubos de los numeros del 1 al 5: \n{cubos}\n')
    print(f'\nDiccionario con el alfabeto: \n{alfabeto}\n')
    print(f'\nLista de numeros impares del 1 al 15: \n{impares}\n')
    print(f'\ntuplas (x: x^3) para nueros impares del 1 al 10: \n{cubosImpares}\n')


if __name__ == '__main__':
    main()

