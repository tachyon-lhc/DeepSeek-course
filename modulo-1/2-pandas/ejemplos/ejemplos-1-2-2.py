import pandas as pd

# Ejemplo 1: Ordenar productos por precio (de menor a mayor)
productos = {
    'Nombre': ['lampara', 'televisor', 'carpeta', 'radio', 'auriculares'],
    'Precio': [20, 300, 5, 45, 30],
    'stock': [10, 4, 50, 15, 30],
    'categoria': ['electronica', 'electronica', 'oficina', 'electronica', 'accesorios']
}

df = pd.DataFrame(productos)

# Ordenar por precio ascendente
df_ordenado = df.sort_values(by='Precio', ascending=True)
print("Productos ordenados por precio (ascendente):")
print(df_ordenado)

# Ejemplo 2: Encontrar el producto más caro y el más barato
# Producto más barato
indice_barato = df['Precio'].idxmin()
producto_barato = df.loc[indice_barato, 'Nombre']
precio_barato = df.loc[indice_barato, 'Precio']

# Producto más caro
indice_caro = df['Precio'].idxmax()
producto_caro = df.loc[indice_caro, 'Nombre']
precio_caro = df.loc[indice_caro, 'Precio']

print(f"El producto más barato es {producto_barato} con un precio de {precio_barato}")
print(f"El producto más caro es {producto_caro} con un precio de {precio_caro}")

# Ejemplo 3: Calcular el total de stock disponible
total_stock = df['stock'].sum()
print(f"El total de stock disponible es: {total_stock}")
