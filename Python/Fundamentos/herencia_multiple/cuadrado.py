from figura_geometrica import FiguraGeometrica
from color import Color

class Square(FiguraGeometrica, Color):
    def __init__(self, side, color):
        FiguraGeometrica.__init__(self, side, side)
        Color.__init__(self, color)
    def area(self):
        return self.getHeight() * self.getWidth()
    def __str__(self):
        return FiguraGeometrica.__str__(self) + ', ' + Color.getColor(self)
    
