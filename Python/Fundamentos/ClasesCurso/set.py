# Set es una coleccion sin orden, indices ni elementos repetidos
# Los elementos de un set no se pueden modificar pero si añadir nuevos o eliminar
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
print(len(planetas))

# Revisar si un elemento esta en el set
if 'Jupiter' in planetas:
    print('Jupiter esta en el set')
else:
    print('Jupiter no esta en el set')
# Revisar de otra forma mas facil (Te devuelve un booleano)
print('Jupiter' in planetas)

# Agregar (No funciona .append, debe ser .add)
planetas.add('Tierra')
print(planetas)
planetas.add('Tierra') # No se pueden añadir elementos repetidos
print(planetas)

# Agregar una lista al set
print('---------------------------------')
morePlanets = ['Pluto', 'Saturn']
planetas.update(morePlanets)
print(planetas)
print('---------------------------------')

# Eliminar con .remove da excepcion
planetas.remove('Tierra')
print(planetas)
# Eliminar con .discard no da excepcion
planetas.discard('Jupiter')
print(planetas)

# Limpiar el set completamente
planetas.clear()
print(planetas)

# Eliminar el set completo
del planetas
print(planetas)