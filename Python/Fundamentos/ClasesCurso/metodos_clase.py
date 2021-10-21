class myClass:
    classVariable = 'Class variable'
    def __init__(self):
        self.instanceVariable = 'Instance variable'
    @staticmethod
    def staticMethod():
        print('Static method')
        print(myClass.classVariable)
        # Desde un metodo estatico no se puede acceder a una variable de instancia
        # print(myClass.instanceVariable)
    @classmethod
    def classMethod(cls):
        print('Class method' + str(cls))
        print(cls.classVariable)
        # No podemos acceder a la variable de instancia desde contexto estatico
        # print(cls.instanceVariable)
    def instanceMethod(self):
        self.staticMethod()
        self.classMethod()
        print(self.classVariable)
        print(self.instanceVariable)
        
myClass.staticMethod()
myClass.classMethod()
print('--------------------------')
objeto1 = myClass()
objeto1.instanceMethod()