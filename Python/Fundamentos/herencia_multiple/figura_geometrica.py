# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    def __str__(self):
        return 'Width: ' + str(self.__width) + ', Height: ' + str(self.__height)
    @abstractmethod
    def area(self):
        pass
    def getWidth(self):
        return self.__width
    def setWidth(self, w):
        self.__width = w        
    def getHeight(self):
        return self.__height
    def setHeight(self, h):
        self.__height = h

