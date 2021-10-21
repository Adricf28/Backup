class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcularArea(self):
        return self.base * self.altura
    
valorBase = int(input('Base de un rectangulo: '))
valorAltura = int(input('Altura de un rectangulo: '))
operacion = Rectangulo(valorBase, valorAltura)
print('El area de su rectangulo es:', operacion.calcularArea())
