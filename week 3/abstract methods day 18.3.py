from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod     # This will force the following inherited classes to use the same functions
    def area(self):
        return 0

class triangle(shape):
    def __init__(self):
        self.base = 5
        self.height = 10

    # If this is not used then it will throw an error
    def area(self):
        return 0.5 * self.base * self.height


shapeA = triangle()
print(f'area of shapeA which is triangle is {shapeA.area()}')


