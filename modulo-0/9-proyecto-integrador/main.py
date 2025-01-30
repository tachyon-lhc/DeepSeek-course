import csv, json, threading
from collections import Counter

class Client:
    def __init__(self, file_clients_name):
        self.file_clients_name = file_clients_name
        self.dataClients = None

    def readClients(self):
        if self.dataClients is None:
            try:
                with open(self.file_clients_name, 'r', encoding='utf-8') as fl:
                    reader = csv.DictReader(fl)
                    self.dataClients = list(reader)

            except FileNotFoundError:
                print('Archivo no encontrado')

        return self.dataClients
    
    def showClients(self):
        if self.dataClients is None:
            self.readClients()

        data = self.dataClients
        i = 1
        for row in data:
            print(f"{i} - Nombre: {row['nombre']} | Edad: {row['edad']}")
            i += 1

class Product:
    def __init__(self, file_products_name):
        self.file_products_name = file_products_name
        self.dataProducts = None

    def readProducts(self):
        if self.dataProducts is None:
            try:
                with open(self.file_products_name, 'r', encoding='utf-8') as fl:
                    reader = csv.DictReader(fl)
                    self.dataProducts = list(reader)

            except FileNotFoundError:
                print('Archivo no encontrado')

        return self.dataProducts
    
    def showProducts(self):
        if self.dataProducts is None:
            self.readProducts()

        data = self.dataProducts
        i = 1
        for row in data:
            print(f"{i} - Nombre: {row['nombre']} | Precio: {row['precio']}")
            i += 1

    def updateProducts(self, data):
        with open(self.file_products_name, 'w', encoding='utf-8', newline='') as fl:
            writer = csv.DictWriter(fl, fieldnames=['nombre', 'precio'])
            writer.writeheader()
            writer.writerows(data)

    def addProduct(self, name, price):
        if self.dataProducts is None:
             self.readProducts()
        data = self.dataProducts

        verify = True
        for row in data:
            if row['nombre'] == name:
                verify = False
        if verify:
            data.append({'nombre': name, 'precio': price})
            self.updateProducts(data)
            print('Producto agregado con éxito')
            return
        print('El producto ya se encuentra')
        return

    def deleteProduct(self, name):
        if self.dataProducts is None:
            self.readProducts()
        data = self.dataProducts

        for row in data:
            if row['nombre'] == name:
                data.remove(row)
                self.updateProducts(data)
                print(f'Producto {name} eliminado')
                return
        print(f'Producto {name} no encontrado')
        return

class Ventas(Client, Product):
    def __init__(self, file_clients_name, file_products_name, file_ventas_name):
        Client.__init__(self, file_clients_name)
        Product.__init__(self, file_products_name)
        self.file_ventas_name = file_ventas_name
        self.ventas = []

    def completeSale(self, cliente, producto):
        data_clients = self.readClients()
        data_products = self.readProducts()

        clientFinder = any(row['nombre'] == cliente for row in data_clients)
        if not clientFinder:
            print(f'El cliente {cliente}, no fue encontrado.')
            return

        productFinder = None
        for row in data_products:
            if row['nombre'] == producto:
                productFinder = row
                break
        
        if productFinder is None:
            print(f'Producto {producto}, no fue encontrado.')
            return

        self.ventas.append({'cliente': cliente, 'producto': producto})
        self.deleteProduct(producto)
        self.updateSales(self.ventas)
        data_products = self.readProducts
        print(f"Venta completada para el cliente {cliente} con el producto {producto}")
        print(self.ventas)

    def updateSales(self, data):
        try:
            with open(self.file_ventas_name, 'w', encoding='utf-8') as fl:
                json.dump({'ventas': data}, fl, indent=4)
        except FileNotFoundError:
            print('Archivo no encontrado')

    def readSales(self):
        try:
            with open(self.file_ventas_name, 'r', encoding='utf-8') as fl:
                data = json.load(fl)
                ventas = data.get('ventas', [])

                contador_ventas = Counter(venta['producto'] for venta in ventas)
                
                return contador_ventas

        except FileNotFoundError:
            print('Archivo no encontrado')
            return []
        except json.JSONDecodeError:
            print('Error al decodificar el archivo JSON')
            return []

    def ventas_mas_populares(self, top_n=5):
        contador_ventas = self.readSales()

        if not contador_ventas:
            print("No hay ventas registradas aún.")
            return

        print(f"Top {top_n} productos más vendidos:")
        for producto, cantidad in contador_ventas.most_common(top_n):
            print(f"{producto}: {cantidad} ventas")

def main():
    # Archivos de datos
    file_clients = 'archivos/clientes.csv'
    file_products = 'archivos/productos.csv'
    file_ventas = 'archivos/ventas.json'

    # Instancias de clases
    MyClients = Client(file_clients)
    MyProducts = Product(file_products)

    # Lectura de datos
    data_clients = MyClients.readClients()
    data_products = MyProducts.readProducts()

    # Mostrar datos
    MyClients.showClients()
    print()
    MyProducts.showProducts()
    print()

    # Instancia de Ventas
    MyVentas = Ventas(file_clients, file_products, file_ventas)

    # Ejecución de ventas en hilos separados
    def execute_sales():
        MyVentas.completeSale('Juan', 'silla')
        MyVentas.completeSale('Pedro', 'ropero')
        MyVentas.completeSale('Sofia', 'cama')
        MyVentas.completeSale('Ana', 'televisor')

    sales_thread = threading.Thread(target=execute_sales)
    sales_thread.start()
    sales_thread.join()

    # Agregar productos
    MyProducts.addProduct('silla', 300)
    MyProducts.addProduct('linterna', 30)
    MyProducts.showProducts()

    # Mostrar ventas
    print('Ventas: ')
    print(MyVentas.readSales())

    # Mostrar ventas mas populares
    MyVentas.ventas_mas_populares()

if __name__ == '__main__':
    main()
