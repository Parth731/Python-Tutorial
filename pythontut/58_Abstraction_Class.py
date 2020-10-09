'''

from abc import  ABC,abstractmethod

    class shape(ABC):

import abstracting this method also used

any function is inheritance to ABC Meta class.  this class inside the
function(method) compulsory run

'''

from abc import  ABCMeta,abstractmethod
# from abc import  ABC,abstractmethod

class shape(metaclass=ABCMeta):
# class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class  Rectangle(shape):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    # here commented printarea function error generated
    #  error: Can't instantiate abstract class Rectangle with abstract methods printarea
    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

# can not create object directly
tryobj = shape()