from usuario import Usuario
from usuario_dao import UsuarioDao
from logger_base import log
import time

while True:
    time.sleep(0.8)
    print("""\nOpciones:
    1- Listar usuarios
    2- Agregar usuario
    3- Actualizar usuario
    4- Eliminar usuario
    5- Salir""")
    opcion = int(input('Elige una opcion: '))
    
    if opcion == 1:
        time.sleep(0.1)
        seleccionar = UsuarioDao.seleccionar()
        for i in seleccionar:
            log.info(i)
        continue
            
    elif opcion == 2:
        agregar = Usuario(username=input('Username: '), password=input('Password: '))
        usuarios_insertados = UsuarioDao.insertar(agregar)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
        continue
        
    elif opcion == 3:
        id = input('ID a actualizar: ')
        actualizar = Usuario(username=input('Username: '), password=input('Password: '), id_usuario=id)
        usuarios_actualizados = UsuarioDao.actualizar(actualizar)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
        continue
        
    elif opcion == 4:
        eliminar = Usuario(id_usuario=int(input('ID a eliminar: ')))
        usuarios_eliminados = UsuarioDao.eliminar(eliminar)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
        continue
        
    elif opcion == 5:
        log.debug('Saliendo del programa...')
        time.sleep(0.5)
        break
    else:
        log.debug('Elige una opcion valida.')