class Array:
    def __init__(self, capacity, fill_value=None):
        self.items=list()
        for i in range(capacity):
            self.items.append(fill_value) 
     
    # Para conocer el tamano del array, el cual será un metodo privado    
    def __len__(self):
        return len(self.items)
    
    # Para representar como un string sus elementos
    def __str__(self):
        return str(self.items)
    
    # Para tener un iterador
    def __iter__(self):
        return iter(self.items)
    
    # Para obtener un elemento en patrticular del array
    def __getitem__(self, index):
        return self.items[index]
    
    # Para reemplazar elementos
    def __setitem__(self, index, new_item):
        self.items[index] = new_item