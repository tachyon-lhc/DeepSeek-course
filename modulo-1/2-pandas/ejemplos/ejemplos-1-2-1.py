import pandas as pd

# Ejemplo 1: Crear un DataFrame
# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(data)
print(df)

# Ejemplo 2: Leer un Archivo CSV
# Leer un archivo CSV
df = pd.read_csv('archivos/datos.csv')
print(df.head())  # Mostrar las primeras filas

# Ejemplo 3: Filtrado de Datos
# Filtrar filas donde la edad es mayor que 30
df_filtrado = df[df['edad'] > 30]
print(df_filtrado)

# Ejemplo 4: Agrupación y Agregación
# Agrupar por ciudad y calcular la media de edad
df_agrupado = df.groupby('Ciudad')['Edad'].mean()
print(df_agrupado)

# Ejemplo 5: Creacion de una serie
serie = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(serie)

# Ejemplo 6: Manipulacion de una DataFrame
# Acceder a una columna
print(df['Nombre'])

# Acceder a una fila específica
print(df.iloc[1])  # Segunda fila

# Modificar un valor
df.at[0, 'Edad'] = 26
print(df)
