import pandas as pd
'''
Ejercicio 1: Crear un DataFrame
    Crea un DataFrame con las siguientes columnas:

        Nombre: ['Ana', 'Juan', 'Laura', 'Pedro']

        Edad: [23, 30, 27, 35]

        Ciudad: ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
'''
data = {'Nombre':['Ana', 'Juan', 'Laura', 'Pedro'],
        'Edad': [23, 30, 27, 35], 
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}

dataFrame = pd.DataFrame(data)

'''
Ejercicio 2: Leer un Archivo CSV

   - Descarga el archivo CSV desde este enlace y cárgalo en un DataFrame.
   - Muestra las primeras 5 filas.
'''
datos = 'archivos/datos_2.csv'
df = pd.read_csv(datos)
first_five_rows = df.head(5)

'''
Ejercicio 3: Filtrado de Datos
    Filtra las filas del DataFrame del Titanic donde la columna Survived es igual a 1 (sobrevivieron).
'''
titanic = 'archivos/datos_2.csv'
df_t = pd.read_csv(titanic)

supervivientes = df_t[df_t['Survived'] == 1]
print(supervivientes)

'''
Ejercicio 4: Agrupación y Agregación
    Agrupa los datos del Titanic por la columna Pclass (clase) y calcula la media de la columna Age (edad).
'''
df_t_agrupado = df_t.groupby('Pclass')['Age'].mean()

def main():
    print(f"De diccionario: \n{data}\n A data frame: \n {dataFrame}")
    print(f"\nPrimeras 5 filas del dataframe de los tripulantes del titanic: \n{first_five_rows}")
    print(f"\nLista de los supervivientes: {supervivientes}")
    print(f"\nPromedio de edad segun la clase de la tripulacion(1,2,3): \n{df_t_agrupado}")

if __name__ == '__main__':
    main()
