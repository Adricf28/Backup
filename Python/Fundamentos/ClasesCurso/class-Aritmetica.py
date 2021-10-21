class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    def sumar(self):
        '''Se realiza la operacion con los atributos de la clase''' # Nueva forma de comentar (''')
        return self.operando1 + self.operando2
    
# Nuevo objeto
aritmetica = Aritmetica(2, 4)
print('Resultado suma:', aritmetica.sumar())