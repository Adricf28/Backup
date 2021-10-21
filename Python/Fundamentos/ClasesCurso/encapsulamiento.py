class Person:
    def __init__(self, name):
        self.__name = name  # Doble guion bajo para que no sea accesible directamente
        self.__age = 18  #Puedes darle valor a un atributo sin definirlo en el init
    def get_name(self):  # Get accede a la informacion del atributo privado
        return self.__name  # Debe usarse return para que te devuelva la info
    def set_name(self, n):  # Set modifica la informacion del atributo privado
        self.__name = n
    def get_age(self):
        return self.__age
    def set_age(self, a):
        self.__age = a
  
p1 = Person('William')
#print(p1.__name) Ya no se usa esta forma porque esta restringida la entrada directa
print(p1.get_name())  # Se accede indirectamente a traves de la segunda funcion

#p1.name = 'Jacob'  # Igualmente da error porque no se puede modificar directamente
#print(p1.__name)

p1.set_name('Christian') # Modifico con set
print(p1.get_name())     # Accedo a la info con get

print(p1.get_age())
p1.set_age(22)
print(p1.get_age())