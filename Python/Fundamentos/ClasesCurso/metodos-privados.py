class Person:
    def __init__(self,name, f_surname, m_surname):
        self.name = name # Sin guiones bajos despues del self = atributo publico
        self._f_surname = f_surname # Un guion bajo = parcialmente privado (protegido)
        self.__m_surname = m_surname # Doble guion bajo = privado
    def public_Method(self): # Se debe crear un metodo publico para acceder al privado
        self.__private_Method()
    def __private_Method(self): # Se pueden crear metodos privados tambien, igual que atributos
        print(self.name)
        print(self._f_surname)
        print(self.__m_surname)
    def get_m_surname(self):
        return self.__m_surname
    def set_m_surname(self, s):
        self.__m_surname = s
        
        
p1 = Person('Juan', 'Lopez', 'Perez')
#p1.__private_Method() # No se puede acceder a un metodo privado
p1.public_Method() # Se debe mandar a llamar al metodo publico para acceder al privado
print(p1.name)
print(p1._f_surname) # Se puede acceder al metodo protegido directamente, pero no deberia
#print(p1.__m_surname) # No se puede acceder directamente
print('--------------------------------------')
p1.set_m_surname('Rodriguez')
print(p1.get_m_surname())
p1.public_Method()



    