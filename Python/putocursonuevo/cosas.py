print('----------------------------------------------------')
# El asterisco convierte al argumento en tupla
def argVar(*args):  
    for i in args:
        print(i)


argVar('Paco', 'Pepe', 'Wan')


print('----------------------------------------------------')
# Kwargs = Keywords Arguments, # El doble asterisco convierte al argumento en diccionario
def argVar2(**kwargs):  
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

argVar2(
    IDE='Integrated Development Environment',
    OVNI='Objeto Volador No Identificado'
)


print('----------------------------------------------------')
# Con encoding='utf8' se pueden leer acentos en los archivos de texto
archivo = open('prueba.txt', 'r', encoding='utf8')
print(archivo.read())
archivo.close()


print('----------------------------------------------------')
with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

class ManejoArchivos():
    def __init__(self,nombre):
        self.nombre = nombre
    
    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        
    def __exit__(self,tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()
            
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())