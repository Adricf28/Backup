from logger_base import logger

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        
    def __str__(self):
        return (
            f'ID Persona: {self.__id_persona}, '
            f'Nombre: {self.__nombre}, '
            f'Apellido: {self.__apellido}, '
            f'Email: {self.__email}'
        )
        
    def getID(self):
        return self.__id_persona
    def setID(self,id):
        self.__id_persona = id
    def getNombre(self):
        return self.__nombre
    def setNombre(self,n):
        self.__nombre = n
    def getApellido(self):
        return self.__apellido
    def setApellido(self,a):
        self.__apellido = a
    def getEmail(self):
        return self.__email
    def setEmail(self,e):
        self.__email = e
        
if __name__ == '__main__':
    persona1 = Persona(1,'Juan','Perez','jperez@gmail.com')
    logger.debug(persona1)
    # Para evitar insertar el id_persona(ya que lo proporciona la BD automaticamente) hay dos formas, puedes darle el valor de None
    persona2 = Persona(None,'Manolo','Lama','melama@gmail.com')
    logger.debug(persona2)
    # O especificar cada parametro, evitando el orden en el que se supone que hay que insertarlos. Aunque para esto hay que darle el valor de none a todos los parametros cuando se definen en el init
    # Esta manera es una mierda, mejor la otra mas sencilla, rapida y directa
    persona3 = Persona(nombre='Paco',apellido='Gonzales',email='pacogo@gmail.com')
    logger.debug(persona3)