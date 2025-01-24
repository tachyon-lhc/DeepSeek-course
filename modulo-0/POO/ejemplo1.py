# EJEMPLO de clases, herencias, decoradores
class Dataset:
    def __init__(self, data):
        """
        Inicializa el dataset.
        :param data: Lista de diccionarios, donde cada diccionario representa una fila.
        """
        self.data = data
    
    def get_summary(self):
        """
        Devuelve un resumen de los datos.
        """
        if not self.data:
            return "El dataset está vacío."
        
        # Obtener las claves (columnas) del primer diccionario
        columns = self.data[0].keys()
        summary = {}
        
        for col in columns:
            # Extraer valores de la columna
            values = [row[col] for row in self.data if col in row]
            
            # Calcular estadísticas básicas
            if all(isinstance(v, (int, float)) for v in values):
                summary[col] = {
                    "min": min(values),
                    "max": max(values),
                    "promedio": sum(values) / len(values)
                }
            else:
                summary[col] = "Columna no numérica"
        
        return summary
    
    def filter_by_column(self, column, value):
        """
        Filtra las filas donde la columna coincide con el valor dado.
        """
        return [row for row in self.data if row.get(column) == value]

# Uso
data = [
    {"nombre": "Alice", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Bob", "edad": 30, "ciudad": "Barcelona"},
    {"nombre": "Charlie", "edad": 35, "ciudad": "Madrid"}
]

dataset = Dataset(data)
print("Resumen:", dataset.get_summary())
print("Filtrado (ciudad = Madrid):", dataset.filter_by_column("ciudad", "Madrid"))