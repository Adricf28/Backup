from logger_base import logger
from psycopg2 import pool
import sys   

class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                                            cls.__MIN_CON,
                                            cls.__MAX_CON,
                                            host=cls.__HOST,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)
                logger.debug(f'Creacion de pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as error:
                logger.error(f'Error al crear el pool de conexiones: {error}')
                sys.exit()
        else:
            return cls.__pool
    
    @classmethod
    def obtenerConexion(cls):
        # Obtener una conexion del pool
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f'Se abrio el cursor con exito: {cls.__cursor}')
                return cls.__cursor
            except Exception as error:
                logger.error(f'Error al ejecutar el cursor: {error}')
                sys.exit()
        else:
            return cls.__cursor
        
    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as error:
                logger.error(f'Error al cerrar cursor: {error}')
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as error:
                logger.error(f'Error al cerrar conexion: {error}')
        logger.debug('Se han cerrado los objetos conexion y cursor')
                
if __name__ == '__main__':
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrar()