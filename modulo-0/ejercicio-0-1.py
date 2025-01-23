'''
En este ejercicio tendremos que crear una class
que se encargue de limpiar los datos de un dateset 
para poder usarlo luego. Elimina las filas repetidas
y rellena datos faltantes con datos pro defecto 
'''
class DataCleaner:
    def __init__(self, data):
        self.data = data

    def log_row_count(func):
        def wraper(self, *args, **kwargs):
            print(f'Fila antes de {func.__name__}: {len(self.data)}')
            result = func(self, *args, **kwargs)
            print(f'Filas despues de {func.__name__}: {len(self.data)}')
            return result
        return wraper

    @log_row_count
    def remove_duplicates(self):
        unique_data = []
        seen = set()

        for row in self.data:
            row_tuple = tuple(row.items())
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)

        self.data = unique_data

    @log_row_count
    def fill_missing_values(self, default_value):
        for row in self.data:
            for key in row:
                if row[key] is None:
                    row[key] = default_value

# Dataset de prueba
data = [
    {"nombre": "Alice", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Bob", "edad": 30, "ciudad": "Barcelona"},
    {"nombre": "Alice", "edad": 25, "ciudad": "Madrid"},  # Duplicado
    {"nombre": "Charlie", "edad": None, "ciudad": "Valencia"},  # Valor faltante
    {"nombre": "David", "edad": 40, "ciudad": None}  # Valor faltante
]

# Crear instancia de DataCleaner
cleaner = DataCleaner(data)

# Eliminar duplicados
cleaner.remove_duplicates()

# Rellenar valores faltantes
cleaner.fill_missing_values(default_value="Desconocido")

# Mostrar el dataset limpio
print("Dataset limpio:", cleaner.data) 
