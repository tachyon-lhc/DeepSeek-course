from functools import reduce

# Ejercicio 1: Calular la Suma de los Cuadrados de una Lista
list_nums = [4, 2, 5]
square = list(map(lambda x: x**2, list_nums))
square_sum = reduce(lambda x, y: x + y, square)

# Ejercicio 2: Calcular el Producto de los Números Pares de una Lista
list_nums_2 = [1,2,3,4,5,6]
pair_sum = reduce(lambda x, y: x*y, filter(lambda x: x%2 == 0, list_nums_2))

# Ejercicio 3: Encontrar la Palabra Más Larga en una Lista
list_words = ['valentin', 'tachyon', 'agustina', 'navidad']
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, list_words)

# Ejercicio 4: Concatenar Números de una Lista en una Cadena
list_nums_3 = [1,0,0,1]
concatenate_num = reduce(lambda x, y: str(x) + str(y), list_nums_3)

# Mostrar resultados

def main():
    print(f"\nLa suma de los cuadrados de la lista {list_nums} es: \n{square_sum}")
    print(f"\nEl producto de los numeros pares de la lista {list_nums_2} es: \n{pair_sum}")
    print(f"\nLa palabra mas larga de la lista {list_words} es: \n{longest_word}")
    print(f"\nLa concatenacion de los numeros {list_nums_3} es: \n{concatenate_num}")

if __name__ == '__main__':
    main()

