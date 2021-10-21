class Pruebas:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    def suma(self):
        return self.operando1 + self.operando2
    def resta(self):
        return self.operando1 - self.operando2
    def multiplicacion(self):
        return self.operando1 * self.operando2
    def division(self):
        return self.operando1 / self.operando2
    def modulo(self):
        return self.operando1 % self.operando2
    def exponente(self):
        return self.operando1 ** self.operando2
    
operacion = Pruebas(10, 5)
print('Suma:', operacion.suma())
print('Resta:', operacion.resta())
print('Multiplicacion:', operacion.multiplicacion())
print('Division:', operacion.division())
print('Modulo:', operacion.modulo())
print('Exponente:', operacion.exponente())

print('----------------------------------------------')

operacion2 = Pruebas(6, 2)
print('Suma:', operacion2.suma())
print('Resta:', operacion2.resta())
print('Multiplicacion:', operacion2.multiplicacion())
print('Division:', operacion2.division())
print('Modulo:', operacion2.modulo())
print('Exponente:', operacion2.exponente())