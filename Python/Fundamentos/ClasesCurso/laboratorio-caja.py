class Caja:
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto 
    def calcularVolumen(self):
        return self.largo * self.ancho * self.alto
    
valorLargo = int(input('Largo de una caja: '))
valorAncho = int(input('Ancho de una caja: '))
valorAlto = int(input('Alto de una caja: '))
operacion = Caja(valorLargo, valorAncho, valorAlto)
print('El volumen de su caja es:', operacion.calcularVolumen())