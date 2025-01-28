#1. Multiprocessing: Cálculo de números primos

from multiprocessing import Process, cpu_count

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(rango):
    print(f"Primos en el rango {rango[0]}-{rango[1]}:")
    for n in range(rango[0], rango[1]):
        if es_primo(n):
            print(n, end=" ")
    print()

if __name__ == "__main__":
    rangos = [(2, 50000), (50000, 100000), (100000, 150000), (150000, 200000)]
    procesos = []

    for rango in rangos:
        p = Process(target=contar_primos, args=(rango,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()


# 2. Threading: Simular múltiples descargas

from threading import Thread
import time

def descargar_archivo(archivo):
    print(f"Iniciando descarga: {archivo}")
    time.sleep(3)  # Simula el tiempo de descarga
    print(f"Descarga completa: {archivo}")

archivos = ["archivo1.zip", "archivo2.zip", "archivo3.zip"]

threads = []

for archivo in archivos:
    t = Thread(target=descargar_archivo, args=(archivo,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
