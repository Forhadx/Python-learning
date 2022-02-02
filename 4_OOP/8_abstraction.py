from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    
    @abstractmethod
    def area(self):
        pass
    
class Triangle(Shape):
    def area(self):
        area = .5 * self.dim1 * self.dim2
        print('Triangle: ', area)


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print('Rectangle: ',area)


t = Triangle(2, 3)
t.area()    # Triangle:  3.0

r = Rectangle(4, 5)
r.area()    # Rectangle: 20

'''
    - Shape() class in abstract class now
    - Triangle & Rectangle class must be use the abstract method 
        otherwise give and error
'''