

class ListQueue():
    def __init__(self):
        self.items = []
        self.size = 0
    
    # Método para agregar elementos
    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    # Método para remover elementos
    def dequeue(self):
        # No necesitamos especificar cual, ya que se irá el primero
        data = self.items.pop()
        self.size -= 1
        return data
    
    # Atravesar, o travesia, para recorrer nuestro queue
    def traverse(self):
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])

            