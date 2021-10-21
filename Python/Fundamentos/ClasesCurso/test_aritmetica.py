#import modulo_aritmetica as aritmetica # Si el archivo esta en la misma carpeta
from modulos import modulo_aritmetica as aritmetica # Si esta en otra carpeta
import modulos.modulo_aritmetica as aritmetica # Directamente desde otra carpeta

resultado = aritmetica.sumar(1,2)
print(resultado)

resultado = aritmetica.restar(3,1)
print(resultado)