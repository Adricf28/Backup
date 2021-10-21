from logger_base import logger
from conexion import Conexion
from persona import Persona

class PersonaDAO:
    # DAO = Data Access Object, se encarga de las operaciones CRUD = Create-Read-Update-Delete
    # Que se ejecutan sobre el objeto Persona   
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))  # .mogrify te imprime en la consola cual es la sentencia que se va a ejecutar en postgreSQL
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for i in registros:
            persona = Persona(i[0], i[1], i[2], i[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas
    
    @classmethod
    def insertar(cls,persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            values = (persona.getNombre(),persona.getApellido(),persona.getEmail())
            cursor.execute(cls.__INSERTAR,values)
            conexion.commit()
            return cursor.rowcount
        except Exception as error:
            conexion.rollback()
            logger.error(f'Error al insertar persona: {error}')
        finally:
            Conexion.cerrar()
            
    @classmethod
    def actualizar(cls,persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Nueva persona: {persona}')
            values = (persona.getNombre(), persona.getApellido(), persona.getEmail(), persona.getID())
            cursor.execute(cls.__ACTUALIZAR,values)
            conexion.commit()
            return cursor.rowcount
        except Exception as error:
            conexion.rollback()
            logger.error(f'Error al actualizar: {error}')
        finally:
            Conexion.cerrar()
            
    @classmethod
    def eliminar(cls,persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            values = (persona.getID(),)
            cursor.execute(cls.__ELIMINAR,values)
            conexion.commit()
            return cursor.rowcount
        except Exception as error:
            conexion.rollback()
            logger.error(f'Error al eliminar: {error}')
        finally:
            Conexion.cerrar()
        
if __name__ == '__main__':
    # personas = PersonaDAO.seleccionar()
    # for i in personas:
    #     logger.debug(i)
    
    # persona1 = Persona(nombre='Adrian',apellido='Carmona',email='acarmona@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # logger.debug(f'Registros insertados: {personas_insertadas}')
    
    # persona2 = Persona(nombre='Monica',apellido='Fernandez',email='mfernandez@gmail.com', id_persona=int(input('ID a actualizar: ')))
    # personas_actualizadas = PersonaDAO.actualizar(persona2)
    # logger.debug(f'Personas actualizadas: {personas_actualizadas}')
    
    # persona3 = Persona(id_persona=int(input('ID a eliminar: ')))
    # personas_eliminadas = PersonaDAO.eliminar(persona3)
    # logger.debug(f'Personas eliminadas: {personas_eliminadas}')