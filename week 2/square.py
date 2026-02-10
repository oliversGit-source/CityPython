class Rectangle:
    '''A class representing a square with area and length.'''
    def __init__(self, length = 4, width = 2, colour = "red"):
        self.length = length
        self.width = width
        self.colour = colour

    def area(self):
        '''return the area of the square.'''
        return f"The area of the rectangle is {self.length*self.width}"