class Persona:
    def __init__(self, nombre, apellido, email, id_persona):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__id_persona = int(id_persona)
        
    def __str__(self):
        return f'ID Persona: {self.__id_persona}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Email: {self.__email}'