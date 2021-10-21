import logging as log

log.basicConfig(level=log.DEBUG, # Se establece a que nivel se van a hacer las comprobaciones
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # Se edita como se va a mostrar la informacion
                   datefmt='%I:%M:%S %p',    # Editar el formato en que se ve el tiempo; %I Hora, %M Minutos, %S Segundos, %p Comprobar si es PM o AM
                   handlers=[
                       log.FileHandler('capa_datos.log'), # Mandar la info a otro archivo
                       log.StreamHandler()                # Mandar la info a la consola
                   ])