from class_3 import Node

class Stack():
    def __init__(self):
        # Iniciamos con un valor vacío en la parte de arriba del stack
        self.top = None
        # Tamano del stack, inicializa en cero
        self.size = 0

    def push(self, data):
        # Instanciamos un Node y le pasamos la data, para agregar el valor.
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1
    
    def pop(self):
        # Si hay un elemento en la parte de arriba del stack
        if self.top:
            data = self.top.data
            self.size -= 1

            # Si hay un elemento por encima
            if self.top.next:
                self.top = self.top.next
            # En caso de que nuestro stack quede vacio
            else:
                self.top = None
            # Para que nos retorne que elemento se elimino
            return data
        # En caso de que el stack este vacio
        else:
            return "The stack is empty"

    # Método para conocer el valor que está en top
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    # Método para eliminar todos los valores
    def clear(self):
        while self.top:
            self.pop()
        