# Ejercicio 1: Convertir una Lista de Longitudes de Pies a Metros
long_foot = [6, 4, 10, 9, 4]
long_metros = list(map(lambda x: round(x*0.3048, 2), long_foot))

# Ejercicio 2: Calcular el Cubo de los Números en una Lista
list_nums = [2,3,7,5,10]
nums_cube = list(map(lambda x: x**3, list_nums))

# Ejercicio 3: Convertir una Lista de Palabras a su Longitud
list_words = ['hola', 'ochenta', 'tachyon', 'valentin']
list_long_words = list(map(lambda x: len(x), list_words))

# Ejercicio 4: Sumar Elementos Correspondientes de Dos Listas
nums_1 = [1,2,3,4,5]
nums_2 = [5,4,3,2,1]

perfect_sum = list(map(lambda x, y: x + y, nums_1, nums_2))

# Probar resultados
def main():
    print(f"\nde pies a metros: \n{long_foot} = {long_metros}\n")
    print(f"\nCalclar el cubo de una lista de numeros: \n{list_nums} = {nums_cube}\n")
    print(f"\nLongitudes de las palabras de una lista: \n{list_words} = {list_long_words}\n")
    print(f"\nSumas los numeros de dos listas: \n{nums_1} + {nums_2} = {perfect_sum}\n")

if __name__ == '__main__':
    main()
