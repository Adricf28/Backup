nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
print(nombres)

# Conocer el largo de la lista
print(len(nombres))

# Imprimir un elemento concreto
print(nombres[2])

# Navegacion inversa
print(nombres[-4])

# Imprimir rango
print(nombres[0:2]) # (sin incluir el indice 2)

# Imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3]) # ( sin incluir el indice 3)

# Imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])

# Cambiar los elementos de una lista
nombres [3] = 'Ivone'
print(nombres)

# Iterar la lista
for nombre in nombres:
    print(nombre)

# Revisar si existe un elemento en la lista
if 'Karla' in nombres:
    print('Karla si existe en la lista')
else:
    print('El elemento buscado no existe en la lista')

# Agregar un nuevo elemento a la lista
nombres.append('Lorenzo')
print(nombres)

# Insertar un nuevo elemento en el indice proporcionado
nombres.insert(1, 'Octavio')
print(nombres)

# Remover un elemento
nombres.remove('Octavio')
print(nombres)

# Remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)

# Remover el indice indicado de la lista
del nombres[0]
print(nombres)

# Limpiar todos los elementos de nuestra lista
nombres.clear()
print(nombres)

# Eliminar por completo la lista
del nombres
print(nombres)