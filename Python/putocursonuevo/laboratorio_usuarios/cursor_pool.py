from conexion import Conexion
from logger_base import log

class CursorPool:
    def __init__(self):
        self._conn = None
        self._cursor = None
        
    def __enter__(self):
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor
        
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        if valor_excepcion:
            self._conn.rollback()
            log.error(f'Error al cerrar el cursor: {valor_excepcion}')
        else:
            self._conn.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conn)