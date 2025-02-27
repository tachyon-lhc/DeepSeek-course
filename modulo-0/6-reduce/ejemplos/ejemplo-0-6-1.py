from functools import reduce

# Ejemplo 1: Sumar Todos los Elementos de una Lista
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Output: 15

# Ejemplo 2: Calcular el Producto de Todos los Elementos de una Lista
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # Output: 120

# Ejemplo 3: Encontrar el Máximo de una Lista
numeros = [10, 20, 5, 40, 30]
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(maximo)  # Output: 40

# Ejemplo 4: Concatenar Cadenas de una Lista
palabras = ["hola", " ", "mundo", "!"]
frase = reduce(lambda x, y: x + y, palabras)
print(frase)  # Output: "hola mundo!"
