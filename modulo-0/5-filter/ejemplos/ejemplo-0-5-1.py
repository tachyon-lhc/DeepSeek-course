# Ejemplo 1: Filtrar Números Pares de una Lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4, 6, 8]

# Ejemplo 2: Filtrar Palabras con Más de 5 Letras
palabras = ["python", "java", "c", "c++", "javascript"]
largas = list(filter(lambda palabra: len(palabra) > 5, palabras))
print(largas)  # Output: ['python', 'javascript']

# Ejemplo 3: Filtrar Números Positivos
numeros = [-10, 20, -30, 40, -50]
positivos = list(filter(lambda x: x > 0, numeros))
print(positivos)  # Output: [20, 40]

# Ejemplo 4: Filtrar Elementos que No Son None
datos = [1, None, "hola", 0, None, "mundo"]
filtrados = list(filter(lambda x: x is not None, datos))
print(filtrados)  # Output: [1, 'hola', 0, 'mundo']
