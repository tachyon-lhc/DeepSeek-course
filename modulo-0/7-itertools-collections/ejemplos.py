'''
                    Ejemplos de itertools
'''
import itertools

# Ejemplo 1: Generar Permutaciones
letras = ['a', 'b', 'c']
permutaciones = list(itertools.permutations(letras, 2))
print(permutaciones)  # Output: [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

# Ejemplo 2: Generar Combinaciones
numeros = [1, 2, 3]
combinaciones = list(itertools.combinations(numeros, 2))
print(combinaciones)  # Output: [(1, 2), (1, 3), (2, 3)]

# Ejemplo 3: Producto Cartesiano
colores = ['rojo', 'verde']
tallas = ['S', 'M']
producto = list(itertools.product(colores, tallas))
print(producto)  # Output: [('rojo', 'S'), ('rojo', 'M'), ('verde', 'S'), ('verde', 'M')]

#############################################################################################

'''
                Ejemplos de collections
'''
import collections

# Ejemplo 1: Usar defaultdict
frutas = ['manzana', 'banana', 'naranja', 'manzana', 'banana']
conteo = defaultdict(int)

for fruta in frutas:
    conteo[fruta] += 1

print(conteo)  # Output: defaultdict(<class 'int'>, {'manzana': 2, 'banana': 2, 'naranja': 1})

# Ejemplo 2: Usar Counter
frutas = ['manzana', 'banana', 'naranja', 'manzana', 'banana']
conteo = Counter(frutas)
print(conteo)  # Output: Counter({'manzana': 2, 'banana': 2, 'naranja': 1})

# Ejemplo 3: Usar deque
cola = deque([1, 2, 3])
cola.append(4)  # Añadir al final
cola.appendleft(0)  # Añadir al principio
print(cola)  # Output: deque([0, 1, 2, 3, 4])

