import csv, json, collections, threading

class Data():
    def __init__(self, file_clients_name, file_products_name):
        self.file_clients_name = file_clients_name
        self.file_products_name = file_products_name
        self.dataClients = None
        self.dataProducts = None

    def readClients(self):
        if self.dataClients is None:
            try:
                with open(self.file_clients_name, 'r', encoding='utf-8') as fl:
                    reader = csv.DictReader(fl)
                    self.dataClients = list(reader)

            except FileNotFoundError:
                print('Archivo no encontrado')

        return self.dataClients

    def readProducts(self):
        if self.dataProducts is None:
            try:
                with open(self.file_products_name, 'r', encoding='utf-8') as fl:
                    reader = csv.DictReader(fl)
                    self.dataProducts = list(reader)

            except FileNotFoundError:
                print('Archivo no encontrado')

        return self.dataProducts
    
    def showClients(self):
        if self.dataClients is None:
            self.readClients()

        data = self.dataClients
        i = 1
        for row in data:
            print(f"{i} - Nombre: {row['nombre']} | Edad: {row['edad']}")
            i += 1

    def showProducts(self):
        if self.dataProducts is None:
            self.readProducts()

        data = self.dataProducts
        i = 1
        for row in data:
            print(f"{i} - Nombre: {row['nombre']} | Precio: {row['precio']}")
            i += 1

class Ventas(Data):
    def __init__(self, file_ventas_name):
        super().__init__(file_ventas_name)
        self.ventas = {}

    def completeSale(self, cliente, producto):
        clientes = self.dataClients
        productos = self.dataProducts

        



file_clients = 'archivos/clientes.csv'
file_products = 'archivos/productos.csv'

MyArch = Data(file_clients, file_products)

data_clients = MyArch.readClients()
data_products = MyArch.readProducts()

MyArch.showClients()
print()
MyArch.showProducts()
