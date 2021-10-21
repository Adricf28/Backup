from empleado import Empleado
from gerente import Gerente

def imprimirDetalles(objeto):
    print(objeto)
    print(type(objeto), end='\n\n')
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado1 = Empleado('Juan', 1000.00)
imprimirDetalles(empleado1)

empleado2 = Gerente('Paco', 2000.00, 'Sistemas')
imprimirDetalles(empleado2)