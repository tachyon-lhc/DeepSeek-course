# Ejemplo 1: Convertir una Lista de Temperaturas de Celsius a Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]


# Ejemplo 2: Convertir una Lista de Nombres a Mayúsculas
nombres = ["alice", "bob", "charlie"]
nombres_mayusculas = list(map(lambda nombre: nombre.upper(), nombres))
print(nombres_mayusculas)  # Output: ['ALICE', 'BOB', 'CHARLIE']


# Ejemplo 3: Aplicar una Función Definida con def
def cuadrado(x):
    return x**2

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print(cuadrados)  # Output: [1, 4, 9, 16, 25]


# Ejemplo 4: Usar map con Múltiples Iterables
numeros1 = [1, 2, 3]
numeros2 = [10, 20, 30]
suma = list(map(lambda x, y: x + y, numeros1, numeros2))
print(suma)  # Output: [11, 22, 33]
