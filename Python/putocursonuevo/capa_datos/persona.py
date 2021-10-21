from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
    def __str__(self):
        return (
            f'ID Persona: {self._id_persona}, '
            f'Nombre: {self._nombre}, '
            f'Apellido: {self._apellido}, '
            f'Email: {self._email}'
        )
        
    # Otra forma de definir getters y setters:
    # Property hace que solo se pueda acceder al atributo que corresponda a traves de un metodo
    # Haciendo que se pueda acceder al metodo como si fuera el atributo directamente
    @property   
    def id_persona(self):
        return self._id_persona
    
    # El setter hace igual que property, hace que el atributo solo sea accesible desde aqui
    # Y permitiendo que se puede llamar al metodo como si fuera un atributo
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
        
if __name__ == '__main__':
    persona1 = Persona(1,'Paco','Perez','pperez@sisisi.com')
    print(persona1.nombre) # Accedes al atributo a traves del getter
    persona1.nombre = 'Juan Carlos' # Cambias el atributo a traves del setter
    print(persona1.nombre)