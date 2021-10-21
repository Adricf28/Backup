class Person:
    def __init__(self, name, age, dni):
        self.name = name
        self.age = age
        self.dni = dni
    def getName(self):
        return self.name 
    def getAge(self):
        return self.age
    def getDni(self):
        return self.dni
    def adult(self):
        if self.age >= 18:
            print('Es mayor de edad')
        else:
            print('Es menor de edad')
    def comprobarDni(self):

        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        
                

        if len(self.dni) == 9:

        
            if self.dni[-1].isalpha() and self.dni[:8].isnumeric():
                     letra = tabla[int(self.dni[:8])%23]
           
                     
                     
                     if letra == self.dni[-1] :
                         print('El dni es correcto')       
    
                     else:
                        print('El dni es incorrecto.')
            else:
                print('El dni no es correcto')
            
        else:
            print('La longitud del dni no es correcta')
    


p1 = Person('Josehuan', 74, '48081035H')
p1.comprobarDni()

p2 = Person('Adri', 20, '26838689N')
p2.comprobarDni()
p3 = Person('Joshua', 20, '26838689A')
p3.comprobarDni()
p4 = Person('Brian', 21, '77233186S')
p4.comprobarDni()