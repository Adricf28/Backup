# DAO significa Data Access Object
from conexion import Conexion
from persona import Persona

class PersonaDao:
    __seleccionar = 'SELECT * FROM persona WHERE id_persona IN %s'
    __insertar = 'INSERT INTO persona(id_persona, nombre, apellido, email) VALUES(%s, %s, %s, %s), '
    __actualizar = 'UPDATE persona SET nombre = %s, apellido = %s, email = %S WHERE id_persona = %s'
    __eliminar = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        Conexion.obtenerConexion()
        Conexion.obtenerCursor()
        entrada = input('Selecciona los registros a buscar separados por comas: ')
        tupla = tuple(entrada.split(','))
        llaves_primarias = (tupla,)
        Conexion.__cursor.execute(PersonaDao.__seleccionar, llaves_primarias)
        registros = Conexion.__cursor.fetchall()
        print(registros)
        Conexion.cerrar()
    
    @classmethod
    def insertar(cls, persona):
        cls.persona = persona
        Conexion.obtenerConexion()
        Conexion.obtenerCursor()
        valores = (cls.persona)
        Conexion.__cursor.execute(PersonaDao.__insertar, valores)
        Conexion.__conexion.commit()
        Conexion.cerrar()
        
    @classmethod
    def actualizar(cls, persona):
        cls.persona = persona
        Conexion.obtenerConexion()
        Conexion.obtenerCursor()
        valores = (persona,)
        Conexion.__cursor.execute(PersonaDao.__actualizar, valores)
        Conexion.__conexion.commit()
        Conexion.cerrar()
        
    @classmethod
    def eliminar(cls, persona):
        Conexion.obtenerConexion()
        Conexion.obtenerCursor()
        seleccion = input('Selecciona el id a eliminar: ')
        valores = (seleccion,)
        Conexion.__cursor.execute(PersonaDao.__eliminar, valores)
        Conexion.__conexion.commit()
        Conexion.cerrar()
        
            