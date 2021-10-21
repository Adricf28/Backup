class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return 'Name: ' +  self.__name + ', Age: ' + str(self.__age)