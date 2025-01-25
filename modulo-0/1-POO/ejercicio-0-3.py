import csv

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_csv()

    def read_csv(self):
        data = []

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)

            return data

        except FileNotFoundError:
            print(f"Error: El archivo '{self.file_path}' no existe.")
            return []
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return []

    def mostrar_datos(self):

        if not self.data:
            print('No hay datos aun')
            return

        for row in self.data:
            print(f"{row['nombre']}: ${row['precio']} - {row['cantidad']} Unidades")


    def filter_data(self):
        productos_caros = []
        
        for producto in self.data:
            if int(producto['precio']) > 100:
                productos_caros.append(producto)
        return productos_caros

    def agregar_producto(self, producto):

        if any(item['nombre'] == producto['nombre'] for item in self.data):
            print('El producto ya se encuentra en la lista')
            return

        self.data.append(producto)

        try:
            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                fieldnames = ['nombre', 'precio', 'cantidad']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.data)
            print(f"Producto '{producto['nombre']}' añadido correctamente.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
         

file = 'productos.csv'

csv_handler = CSVHandler(file)

csv_handler.mostrar_datos()

productos_caros = csv_handler.filter_data()
print(f'Productos caros: {productos_caros}')

# Añadir un nuevo producto
nuevo_producto = {'nombre': 'Impresora', 'precio': '200', 'cantidad': '8'}
csv_handler.agregar_producto(nuevo_producto)

csv_handler.mostrar_datos()

