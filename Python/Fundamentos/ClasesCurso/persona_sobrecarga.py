class Persona:
    def __init__(self, age):
        self.__age = age
        
    def __add__(self, otro): # add se usa para sumar objetos
        return self.__age + otro.__age
    
    def __sub__(self, otro): # sub se utiliza para restar objetos 
        return self.__age - otro.__age
    
    def __mul__(self, otro): # mul para multiplicar
        return self.__age * otro.__age
    
    def __truediv__(self, otro): # truediv para dividir
        return self.__age / otro.__age
    
    def __mod__(self, otro): # mod para modulos
        return self.__age % otro.__age
    
    def __pow__(self, otro): # pow para exponentes
        return self.__age ** otro.__age
    
    def __lt__(self, otro): # lt para <
        return self.__age < otro.__age
    
    def __gt__(self, otro): # gt para >
        return self.__age > otro.__age
    
    def __le__(self, otro): # le para <= 
        return self.__age <= otro.__age
    
    def __ge__(self, otro): # ge para >=
        return self.__age >= otro.__age
    
    def __eq__(self, otro): # eq para ==
        return self.__age == otro.__age
    
    def __ne__(self, otro): # ne para !=
        return self.__age != otro.__age
        
        
persona1 = Persona(4)
persona2 = Persona(2)
print('4 + 2: ', persona1 + persona2)
print('4 - 2: ', persona1 - persona2)
print('4 * 2: ', persona1 * persona2)
print('4 / 2: ', persona1 / persona2)
print('4 % 2: ', persona1 % persona2)
print('4 ** 2: ', persona1 ** persona2)
print('4 < 2: ', persona1 < persona2)
print('4 > 2: ', persona1 > persona2)
print('4 <= 2: ', persona1 <= persona2)
print('4 >= 2: ', persona1 >= persona2)
print('4 == 2: ', persona1 == persona2)
print('4 != 2: ', persona1 != persona2)





