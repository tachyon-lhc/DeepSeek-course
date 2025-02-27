# Crea una función lambda que reste dos números.
resta = lambda a, b: a - b

# Crea una función lambda que calcule el cubo de un número.
cubo = lambda x: x**3

# Crea una función lambda que calcule el área de un triángulo (área = (base * altura) / 2)
area_triangulo = lambda base, altura: (base * altura)/2

# Crea una función lambda que devuelva "Positivo" si un número es mayor que 0, "Negativo" si es menor que 0 y "Cero" si es igual a 0.
pos_o_neg = lambda x: "Positivo" if x >= 0 else "Negativo"

# Crea una función lambda que tome una cadena de texto y devuelva la cadena en mayúsculas.
toMayus = lambda str: str.upper()

def main():
    #Cargar datos

    resta_1 = resta(5,2) #3
    cubo_1 = cubo(3) #27
    area_triangulo_1 = area_triangulo(2, 5) #5
    positivo_o_negativo_1 = pos_o_neg(4) #Positivo
    min_to_mayus = toMayus('hola') #HOLA

    #mostrar resultados
    print(f'\nresta 5 -2 = {resta_1}\n')
    print(f'\n3^3 = {cubo_1}\n')
    print(f'\nArea de triangulo (2, 5) = {area_triangulo_1}\n')
    print(f'\nel numero 4 es: {positivo_o_negativo_1}\n')
    print(f'\nhola: {min_to_mayus}\n')

if __name__ == "__main__":
    main()
