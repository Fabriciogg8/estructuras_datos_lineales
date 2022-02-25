import random
from class_1 import Array

class Cube:
    def __init__(self, rows, columns, sides, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for col in range(columns):
                self.data[row][col] = Array(sides, fill_value)
   

    def get_height(self):
        ''' Returns the number of rows of the cube '''
        return len(self.data)

    def get_width(self):
        ''' Returns the number of columns of the cube '''
        return len(self.data[0])
    
    def get_sides(self):
        '''Returns the number of sides of the cude '''
        return len(self.data[0][0])

    def __get_item__(self, index):
        ''' Supports two-dimensional indexing with [row][columns] '''
        return self.data[index]

    def __str__(self):
        ''' Return a string representation of the grid '''
        result = ''

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for side in range(self.get_sides()):
                    result += str(self.data[row][col][side]) + " "
                result += "\n"

        return str(result)


if __name__ == "__main__":
    cubo = Cube(5,5,8)
    print(cubo)
    