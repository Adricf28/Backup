from numeros_identicos_exception import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('Numeros identicos')
    resultado = a / b
except ZeroDivisionError as e:
    print(type(e))
    print(f'Ocurrió el siguiente error con ZeroDivisionError: {e}')
except TypeError as e:
    print(type(e))
    print(f'Ocurrió el siguiente error con TypeError: {e}')  # Hay que poner las excepciones de menor a mayor jerarquia
except ValueError as e:
    print(type(e))
    print(f'Ocurrió el siguiente error con ValueError: {e}')    
except Exception as e:                                      # Porque sino, la de mayor jerarquia absorberia a las demas
    print(type(e))                                          # Dejando inutil las especificaciones de error   
    print(f'Ocurrió el siguiente error con Exception: {e}')
else:
    print(f'No hubo errores, su resultado es {resultado}')
finally:
    print('Fin del manejo de excepciones.')
       
print('Continuamos...')