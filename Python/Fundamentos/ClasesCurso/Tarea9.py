class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + ', Velocidad(km/h): ' + str(self.velocidad)
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo
    
v1 = Vehiculo('Rojo', 4)
c1 = Coche('Azul', 4, 70)
b1 = Bicicleta('Amarilla', 2, 'De carretera')
print(v1)
print(c1)
print(b1)