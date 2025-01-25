'''
Ejemplo 1: Función Lambda Simple
Crear una función lambda que sume dos números.
''''
suma = lambda x, y: x + y
print(suma(3, 5))  # Output: 8

'''
Ejemplo 2: Función Lambda con un Solo Argumento
Crear una función lambda que calcule el cuadrado de un número.
'''
cuadrado = lambda x: x**2
print(cuadrado(4))  # Output: 16

'''
Ejemplo 3: Función Lambda con Múltiples Argumentos
Crear una función lambda que calcule el área de un rectángulo.
'''
area_rectangulo = lambda base, altura: base * altura
print(area_rectangulo(5, 10))  # Output: 50

'''
Ejemplo 4: Función Lambda con Condicionales
Crear una función lambda que devuelva "Par" si un número es par e "Impar" si es impar.
'''
par_o_impar = lambda x: "Par" if x % 2 == 0 else "Impar"
print(par_o_impar(7))  # Output: Impar
print(par_o_impar(8))  # Output: Par

'''
Ejemplo 5: Función Lambda con Múltiples Expresiones (No Válido)
Las funciones lambda solo pueden tener una expresión. Esto NO es válido:
'''
lambda x: x**2; x**3  # Error: Solo una expresión permitida.
