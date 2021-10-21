# Tupla: mantiene el orden, pero no se puede modificar (Coleccion inmutable)
frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
print(len(frutas))
print(frutas[0])
print(frutas[-3])
print(frutas[:2])

# Cambiar la tupla a lista para poder modificarla
frutasLista = list(frutas)
frutasLista[1] = 'Manzana'
frutas = tuple(frutasLista)
print(frutas)

# Iterar todo en la misma linea, decidiendo que poner al final de cada i
for i in frutas:
    print(i, end=' ')

# No puedes agregar ni eliminar nada de una tupla, pero si eliminar la tupla en sí
del frutas
print(frutas)