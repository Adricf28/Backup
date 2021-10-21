# Un diccionario esta compuesto de llave,valor (key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
print(len(diccionario))

# Acceder a un elemento
print(diccionario['IDE'])
# Otra forma de acceder
print(diccionario.get('IDE'))

# Modificar valores
diccionario['IDE'] = 'Integrated development environment'
print(diccionario['IDE'])

# Iterar
for i in diccionario:  # Iterar llaves
    print(i)
for i in diccionario:  # Iterar valor asociado a cada llave
    print(diccionario[i])    
for valor in diccionario.values(): # Iterar solo los valores, sin las llaves
    print(valor)

# Comprobar existencia de un elemento
print('ID' in diccionario)

# Agregar nuevos elementos
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Remover elementos
print('--------------------------------------------')
diccionario.pop('DBMS')
print(diccionario)
print('--------------------------------------------')

# Limpiar diccionario
# diccionario.clear()
# print(diccionario)

# Eliminar por completo
# del diccionario
# print(diccionario)

#Para borrar un par clave-valor de un diccionario usaremos la sentencia del , y entre corchetes el valor de la clave a borrar.
del diccionario['IDE']
print(diccionario)