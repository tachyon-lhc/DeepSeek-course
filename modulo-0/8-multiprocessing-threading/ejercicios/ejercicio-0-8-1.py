'''
Multiprocessing:

    Calcula el factorial de un rango de números usando múltiples procesos.
    Utiliza una cola para compartir resultados entre procesos.
'''

from multiprocessing import Process, Pool, Queue

def factorial(num):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

if __name__ == '__main__':
    nums = [1,4,5,7,2,8,9]

    with Pool() as p:
        factoriales = p.map(factorial, nums)

    print(factoriales)
