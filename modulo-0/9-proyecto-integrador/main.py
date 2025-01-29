import csv, json, collections, threading

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
        print(f"Venta completada para el cliente {cliente} con el producto {producto}")
        print(self.ventas)

        
file_clients = 'archivos/clientes.csv'
file_products = 'archivos/productos.csv'
file_ventas = 'archivos/ventas.csv'

MyClients = Client(file_clients)
MyProducts = Product(file_products)

data_clients = MyClients.readClients()
data_products = MyProducts.readProducts()

MyClients.showClients()
print()
MyProducts.showProducts()
print()
MyVentas = Ventas(file_clients, file_products, file_ventas)
MyVentas.completeSale('Juan', 'silla')
MyVentas.completeSale('Pedro', 'mesa')
