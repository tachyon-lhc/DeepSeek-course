import pandas as pd

df_p = 'archivos/productos.csv'
df_d = 'archivos/descuentos.csv'
merge = 'archivos/precio_total.csv'

class Producto:
    def __init__(self, file_name_producto):
        self.file_name_producto = file_name_producto
        try:
            self.data_producto = pd.read_csv(file_name_producto)
        except FileNotFoundError:
            print('Archivo no encontrado')

    def show_data_producto(self):
        print(self.data_producto)

    def verify_duplicates(self):
        self.data_producto = self.data_producto.drop_duplicates(subset = 'Nombre')
        print('Nombres duplicados han sido eliminados')
        self.update_data(self.data_producto, self.file_name_producto)
        print(self.data_producto)

    def update_data(self, data, file):
        data.to_csv(file, index=False)
        print('Datos actualizados')

class Descuento(Producto):
    def __init__(self, file_name_producto, file_name_descuento, file_name_merge):
        super().__init__(file_name_producto)
        self.file_name_descuento = file_name_descuento
        self.file_name_merge = file_name_merge
        try:
            self.data_descuento = pd.read_csv(file_name_descuento)
        except FileNotFoundError:
            print("archibo no encontrado")

    def show_data_descuento(self):
        print(self.data_descuento)

    def apply_descuento(self):
        if 'Categoria' not in self.data_producto.columns or 'Categoria' not in self.data_descuento.columns:
            print("Error: La columna 'Categoria' no se encuentra en uno de los DataFrames.")
            return

        merge_data = pd.merge(self.data_producto, self.data_descuento, on='Categoria', how='left')
        merge_data['Precio'] *= (1 - merge_data['Descuento']/100)
        merge_data = merge_data.sort_values(by='Precio', ascending = True)

        print("\n=== DataFrame con Descuento Aplicado y Ordenado ===\n")
        print(merge_data)

        resumen = merge_data.groupby('Categoria').agg(
        precio_promedio_final = ('Precio', 'mean') 
        )
        self.update_data(resumen, self.file_name_merge)
        print("\n=== Resumen por Categoría ===\n")
        print(resumen)

def main():
    MyProduct = Producto(df_p)
    MyDescuento = Descuento(df_p, df_d, merge)
    MyDescuento.apply_descuento()

if __name__ == '__main__':
    main()
