# Ejercicio 1: Filtrar Números Primos
list_nums_1 = [i for i in range(0,40)]

def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
            break
    return True

primos = list(filter(es_primo, list_nums_1))

# Ejercicio 2: Filtrar Palabras que Comienzan con una Letra Específica
list_words_1 = ['hola', 'dia', 'avestruz', 'alba', 'devon']
letra = 'a'
filter_words = list(filter(lambda x: x[:1] == letra, list_words_1))

# Ejercicio 3: Filtrar Elementos Mayores que un Valor
list_nums_2 = [4,6,10,6,25,4,11,8,40,12]
cap_value = 10
filter_nums = list(filter(lambda x: x>cap_value, list_nums_2))

# Ejercicio 4: Filtrar Cadenas No Vacías
list_words_2 = ['ad7a8', 'asdn21', '', 'asdhjk1', ' ']
filter_value_words = list(filter(lambda x: x.strip() != '', list_words_2))

#mostras resultados
def main():
    print(f'\nNumeros primero del 1 al 40: \n{primos}')
    print(f'\nPalabras que comienzan con la letra {letra} en {list_words_1}: \n{filter_words}')
    print(f'\nNumeros mayotes a {cap_value} en {list_nums_2}: \n{filter_nums}')
    print(f'\nCadenas no vacias en {list_words_2}: \n{filter_value_words}')

if __name__ == '__main__':
    main()
