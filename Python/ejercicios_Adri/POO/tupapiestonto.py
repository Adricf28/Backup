class Persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    def getName(self):
        return self.nombre
    def getSurname(self):
        return self.apellido
    def getDni(self):
        return self.dni

class Habitante(Persona):
    def __init__(self,nombre,apellido,dni, tieneCertificado):
        super().__init__(nombre, apellido, dni)
        if tieneCertificado == 'Si':
            self.certificado = True
        else:
            self.certificado = False
    def getCertificado(self):
        return self.certificado
        
        
        
class Ciudad:
    def __init__(self, nombreCiudad):
        self.nombreCiudad = nombreCiudad
    poblacion = []
    def aniadirHabitante(self):
        name = input('Nombre : ')
        surname = input('Apellidos: ')
        dni = input('DNI: ')
        certified = input('Tiene certificado ? ("Si" o "No")')
        h1 = Habitante(name,surname,dni,certified)
        self.poblacion.append(h1)
 
    def mostrarHabitantes(self):
        for i in self.poblacion:
            if i.getCertificado():
                print(i.getCertificado())
                print(i.getName(),i.getSurname(), 'con dni:', i.getDni(),'esta empadronado en ',self.nombreCiudad)
            else:
                print(i.getCertificado())
                print(i.getName(),i.getSurname(), 'con dni:', i.getDni(),'no esta empadronado en ',self.nombreCiudad, ' y sera fusilado en las proximas horas.')
malaga = Ciudad('Malaga')
malaga.mostrarHabitantes()
malaga.aniadirHabitante()
malaga.mostrarHabitantes()
malaga.aniadirHabitante()
malaga.aniadirHabitante()
malaga.mostrarHabitantes()