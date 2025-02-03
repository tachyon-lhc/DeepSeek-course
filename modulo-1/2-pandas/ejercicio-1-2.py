import pandas as pd

'''
Agrega una nueva columna "Categoría" a tu DataFrame de productos y asígnale valores.
'''

productos = {'Nombre': ['lampara', 'televisor', 'carpeta', 'radio', 'auriculares'],
             'Precio': [20, 300, 5, 45, 30]}

df = pd.DataFrame(productos)
df['Stock'] = [10, 4, 50, 15, 30]
df['Categoria'] = ['electronica', 'electronica', 'oficina', 'electronica', 'accesorios']

def filtrar_categoria(df, categoria):
    return(df[df['Categoria'] == categoria])

def filtrar_stock(df, stock):
    return(df[df['stock'] <= stock])

def aplicar_descuento(df, descuento, categoria):
    df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce').astype(float)
    df.loc[df['Categoria'] == categoria, 'Precio'] *= (1 - descuento / 100)
    return df

def ordenarPrecios(df):
    precios_ordenados = df.sort_values(by='Precio', ascending = True)
    print(precios_ordenados)
    id_max = df['Precio'].idxmax()
    id_min = df['Precio'].idxmin()

    producto_max = df.loc[id_max, 'Nombre']
    precio_max = df.loc[id_max, 'Precio']

    produco_min = df.loc[id_min, 'Nombre']
    precio_min = df.loc[id_min, 'Precio']

    print(f"Precio mas alto: {precio_max} - Producto: {producto_max}")
    print(f"Precio mas bajo: {precio_min} - Producto: {produco_min}")

def resumenStock(df):
    suma_stock = df['Stock'].sum()
    promedio_stock = df['Stock'].mean()
    id_stock_max = df['Stock'].idxmax()
    nombre_stock_max = df.loc[id_stock_max, 'Nombre']
    print(f"Suma total de stocks: {suma_stock}")
    print(f"Promedio de stocks generales: {promedio_stock}")
    print(f"Producto con mas stock: {nombre_stock_max}")

def agruparProductos(df):
    stock_categoria = df.groupby('Categoria')['Stock'].sum()
    precio_categoria = df.groupby('Categoria')['Precio'].mean()

    print(f"\nStock total por categoria: \n{stock_categoria}")
    print(f"\nPromedio de precio por categoria: \n{precio_categoria}")

aplicar_descuento(df, 50, 'electronica')
print(df)
