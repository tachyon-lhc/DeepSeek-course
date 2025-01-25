import json

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = []
    
    def añadir_producto(self, nombre, precio, cantidad, file):

        try:
            with open(file, 'r', encoding='utf-8') as fl:
                self.productos = json.load(fl)
        except FileNotFoundError:
            self.productos = []
        except json.JSONDecodeError:
            self.productos = []

        productos = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad,
        }

        self.productos.append(productos)
        self.guardar_inventario(file)

        
    
    def buscar_producto(self, nombre, file):
        with open(file, 'r', encoding='utf-8') as fl:
            self.productos = json.load(fl)

            for producto in self.productos:
                if producto['nombre'] == nombre:
                    return f"Producto: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}"
            return 'producto no encontrado'
    
    def guardar_inventario(self, file):
        with open(file, 'w', encoding='utf-8') as fl:
            json.dump(self.productos, fl, indent=4)
    
    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                self.productos = json.load(file)
        except FileNotFoundError:
            self.productos = []
        except json.JSONDecodeError:
            self.productos = []

# Crear inventario
inventario = Inventario()

file = 'inventario.json'


# Buscar un producto
producto = inventario.buscar_producto("Mouse", file)
print(producto)  # Debe mostrar: Producto: Mouse, Precio: 20, Cantidad: 50

# Guardar inventario en un archivo
inventario.guardar_inventario("inventario.json")

# Cargar inventario desde el archivo
nuevo_inventario = Inventario()
nuevo_inventario.cargar_inventario("inventario.json")