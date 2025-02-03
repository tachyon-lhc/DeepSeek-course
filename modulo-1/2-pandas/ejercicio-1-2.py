import pandas as pd

'''
Agrega una nueva columna "Categoría" a tu DataFrame de productos y asígnale valores.
'''

productos = {'Nombre': ['lampara', 'televisor', 'carpeta', 'radio', 'auriculares'],
             'Precio': [20, 300, 5, 45, 30]}

df = pd.DataFrame(productos)
df['stock'] = [10, 4, 50, 15, 30]
df['categoria'] = ['electronica', 'electronica', 'oficina', 'electronica', 'accesorios']

def filtrar_categoria(df, categoria):
    return(df[df['categoria'] == categoria])

def filtrar_stock(df, stock):
    return(df[df['stock'] <= stock])

def aplicar_descuento(df, descuento):
    df['Precio'] = df['Precio'] - df['Precio']*(descuento/100)
    return df

filtrar_categoria(df, 'electronica')
print()
filtrar_stock(df, 10)
print()
aplicar_descuento(df, 10)
print(df)
