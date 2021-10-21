class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Name: ' + self.name + ', Age: ' + str(self.age)
class Employee(Person): # Entre parentesis la clase de la que hereda
    def __init__(self, name, age, wage): # Hay que definir los valores de la clase padre
        super().__init__(name, age) # Con super se accede a los atributos de la clase padre
        self.wage = wage
    def __str__(self):
        return super().__str__() + ', Wage: ' + str(self.wage)
        
p1 = Person('William', 28)
print(p1)

e1 = Employee('Michael', 25, 2000)
print(e1)

e1.name = 'Anthony'
e1.wage = '1500.00'
print(e1)