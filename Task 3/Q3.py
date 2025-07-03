""" Implement a Python class called ‘Rectangle‘ that has attributes for width
and height. Include methods to calculate the area and perimeter of the rectangle.
Create an instance of the class and demonstrate the methods. """

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2*self.width + 2*self.height
    
r1 = Rectangle(2,4)
print(r1.calculate_area())
print(r1.calculate_perimeter())
