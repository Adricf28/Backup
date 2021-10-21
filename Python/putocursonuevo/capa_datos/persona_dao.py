from cursor_pool import CursorPool
from logger_base import log
from conexion import Conexion
from persona import Persona

class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:  # El with hace que el cursor se abra y se ciere automaticamente y tambien que se haga autocommit
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for i in registros:
                persona = Persona(i[0], i[1], i[2], i[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls,persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount
                
            
    @classmethod
    def actualizar(cls,persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
                
            
    @classmethod
    def eliminar(cls,persona):
        with CursorPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount
            
            
if __name__ == '__main__':
    # persona = PersonaDAO.seleccionar()
    # for i in persona:
    #     log.debug(i)
        
    
    # persona2 = Persona(nombre='Adrian',apellido='Carmona',email='acarmona@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona2)
    # log.debug(f'Personas insertadas: {personas_insertadas}')
    
    
    # persona3 = Persona(31,'sisisi','nonono','sisinono@gmail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona3)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')
    
    
    # persona4 = Persona(31)
    # personas_eliminadas = PersonaDAO.eliminar(persona4)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')
    
    # persona = PersonaDAO.seleccionar()
    # for i in persona:
    #     log.debug(i)