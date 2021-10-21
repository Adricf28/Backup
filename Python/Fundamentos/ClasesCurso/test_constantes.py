from constantes import *  # Con un asterisco importas todo lo que haya en el archivo
from constantes import Matematicas as Mates # Puedes renombrar al importar

print(MI_CONSTANTE)
print(Mates.PI)

MI_CONSTANTE = 'Nuevo valor'  # En python las constantes se pueden modificar 
Mates.PI = 3.14
print(MI_CONSTANTE)
print(Mates.PI)