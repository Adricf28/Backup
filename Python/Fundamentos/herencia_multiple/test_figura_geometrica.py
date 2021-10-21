from cuadrado import Square
s1 = Square(4, 'Red')
print(s1.area())
print(s1.getColor())

# Method Resolution Order .mro
print(Square.mro())

from figura_geometrica import FiguraGeometrica
f1 = FiguraGeometrica(4, 4) # No es posible crear objetos de clases abstractas