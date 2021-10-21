from logger_base import log
from cursor_pool import CursorPool
from usuario import Usuario

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for i in registros:
                usuario = Usuario(i[0], i[1], i[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls,usuario):
        with CursorPool() as cursor:
            values = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, values)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,usuario):
        with CursorPool() as cursor:
            values = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, values)
            return cursor.rowcount
            
    @classmethod
    def eliminar(cls,usuario):
        with CursorPool() as cursor:
            values = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, values)
            return cursor.rowcount