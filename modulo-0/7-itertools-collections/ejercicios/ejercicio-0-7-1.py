import itertools
from collections import defaultdict, Counter, deque

# Ejercicio 1: Generar Todas las Combinaciones de 3 Elementos
numeros = [2,5,1,6,9,2]
tricomb = list(itertools.combinations(numeros, 3))

# Ejercicio 2: Contar la Frecuencia de Caracteres en una Cadena
string = 'Esta es una frase con distinta cantidad frecuencia de caracteres'
conteo = Counter(string.replace(' ',''))

# Ejercicio 3: Usar defaultdict para Agrupar Palabras por Longitud
words = ['hola', 'agustina', 'te', 'quiero']
word_per_len = defaultdict(int)

for word in words:
    for letter in word:
        word_per_len[word]+=1

# Ejercicio 4: Usar deque para Implementar una Cola
cola = deque([i for i in range(14)])



# Mostrar los resultados
def main():
    print(f'combinaciones de 3 elementos de {numeros}:\n{tricomb}\n')
    print(f'La frase "{string}"\n Tiene:\n {conteo}\n esta frecuencia de caracteres\n')
    print(f'Agrupacion de estas palabras: {words} por longitud:\n{word_per_len}\n')
    print(f'Esta es la cola: {cola}\n')
    while True:
        print(f'Alguien fue atendido o alguien ingresó a la cola?')
        state = int(input('1-Atendido  2-Ingreso 3-Salir  '))

        if state == 1:
            cola.popleft()
            print(cola)
        elif state == 2:
            cola.append(int(cola[-1]+1))
            print(cola)
        elif state == 3:
            break
        else:
            print('Ingresa una opcion correcta')

if __name__ == '__main__':
    main()
        



