import psycopg2 as db


class Conexion:
    __database = 'test_db'
    __username = 'postgres'
    __password = 'admin'
    __db_port = '5432'
    __host = '127.0.0.1'
    __conexion = db.connect(__username,
                            __password,
                            __db_port,
                            __host,
                            __database)
    __cursor = __conexion.cursor()

    @classmethod
    def obtenerConexion(cls):
        try:
            Conexion.__conexion
        except Exception as error:
            print(f'Ha ocurrido el siguiente error: {error}')

    @classmethod
    def obtenerCursor(cls):
        try:
            Conexion.__cursor
        except Exception as error:
            print(f'Ha ocurrido el siguiente error: {error}')

    @classmethod
    def cerrar(cls):
        Conexion.__cursor.close()
        Conexion.__conexion.close()


Conexion.obtenerConexion()
