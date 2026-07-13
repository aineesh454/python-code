import math
from abc import ABC, abstractmethod
from typing import override

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @override
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
class triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @override
    def calculate_area(self):
        triangle_area = 0.5 * self.base * self.height
        triangle_area = int(triangle_area)
        return triangle_area
    
class rectangle(Shape):
    def __init__(self, length, breadth):
            self.length = length
            self.breadth = breadth

    @override
    def calculate_area(self):
        return self.length * self.breadth
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    @override
    def calculate_area(self):
        return self.side ** 2
        
shape_list = [Circle(4), triangle(5, 7), rectangle(10,12), Square(6)]


for shape in shape_list:
    area = shape.calculate_area()
    print(f"The area of the {shape.__class__.__name__} is: {area}") 