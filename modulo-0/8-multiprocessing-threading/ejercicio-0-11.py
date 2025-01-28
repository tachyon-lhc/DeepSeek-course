'''
Threading:
        Crea un programa que simule la lectura y escritura en un archivo desde múltiples hilos.
        Implementa un mecanismo con Lock para evitar conflictos al acceder al archivo.
'''

from threading import Thread, Lock
import time

lock = Lock()

def leer_archivo():
    with lock:
        print("Leyendo archivo...")
        time.sleep(2)
        print("Contenido del archivo: Hola Mundo!")

def escribir_archivo():
    with lock:
        print("Escribiendo archivo...")
        time.sleep(2)
        print("Archivo escrito correctamente.")

if __name__ == "__main__":
    t1 = Thread(target=leer_archivo)
    t2 = Thread(target=escribir_archivo)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Operaciones completadas')
