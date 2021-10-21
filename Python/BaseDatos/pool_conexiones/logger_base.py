import logging

logger = logging

logger.basicConfig(level=logging.DEBUG, # Se establece a que nivel se van a hacer las comprobaciones
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s %(message)s]',  # Se edita como se va a mostrar la informacion
                   datefmt='%I:%M:%S %p',    # Editar el formato en que se ve el tiempo; %I Hora, %M Minutos, %S Segundos, %p Comprobar si es PM o AM
                   handlers=[
                       logging.FileHandler('capa_datos.log'), # Mandar la info a otro archivo
                       logging.StreamHandler()                # Mandar la info a la consola
                   ])

if __name__ == '__main__':   # Esto hace que estas lineas solo se ejecuten en este archivo y no al importarlo en otro
    logging.warning('Mensaje a nivel warning')
    logging.info('Mensaje a nivel info')
    logging.debug('Mensaje a nivel debug')
    logging.error('Ocurrio un error en la base de datos')
    logging.debug('Se realizo la conexion con exito')