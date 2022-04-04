from class_1 import Array

class Grid:
    def __init__(self, rows, columns, fill_value=None):
        # Hacemos referencia a un Array y le pasamos como atributo los filas
        self.data = Array(rows)
        for row in range(rows):
            # Cda dato de la fila, contendrá un Array que serán las columnas
            self.data[row] = Array(columns, fill_value)
    
    # A diferencia del array de una dimension, no tendremos solo la longitud, sino altura y ancho.
    def get_height(self):
        return len(self.data)

    # Self.data en el indice cero (o en cualquier índice debería ser lo mismo), porque estamos anidando un array. 
    def get_width(self):
        return len(self.data[0])

    # Para obtener un elemento en patrticular del array
    def __getitem__(self, index):
        return self.data[index]

    # Para representar como un string sus elementos
    def __str__(self):
        result =  ""

        # Con un ciclo for anidado vamos a recorrer las filas y las columnas para obtener ese elemento
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                # El dato en ese indice, lo vamos anadir a la variable result
                result += str(self.data[row][col]) + " "
            # Le agregamos un salto de linea para que quede mas prolijo
            result += "\n"
        # Devolvemos la representación en string de la variable resultado. En str porque 
        # puede que hayamos guardado algun dato númerico
        return str(result)