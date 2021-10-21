class Persona:
    def __init__(this, n, e, *v, **d): # No es obligatorio el self, pero deberia usarlo
     #El asterico significa que es una variable opcional, no salta error si no se le da valor
     # Doble asterisco para diccionarios 
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d
    def desplegar(paco): 
        print('Nombre:', paco.nombre) # Se puede usar cualquier palabra
        print('Edad:', paco.edad) # Siempre y cuando coincida con la de mi funcion
        print('Valores(Tupla):', paco.valores)
        print('Diccionario:', paco.diccionario)

print('------------------------------------------------')
p1 = Persona('Juan', '28')
p1.desplegar() #No hace falta imprimir porque la propia funcion imprime su contenido al llamarla
print('------------------------------------------------')
p2 = Persona('Carla', 30, 2,4,5)
p2.desplegar()
print('------------------------------------------------')
p3 = Persona('Pepe', 32, 4,9, m='Manzana', p='Pera', c='Cereza')
p3.desplegar()    # Para el diccionario, introducir cualquier llave-valor