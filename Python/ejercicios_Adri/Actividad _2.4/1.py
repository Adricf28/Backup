# 1.- Crea un diccionario con 3 cadenas de caracteres leídas por teclado junto con sus claves.
diccionario = {}
while True:
    opcion = int(input('1- Añadir, 2- Listar, 3- Cerrar '))
    if opcion == 1:
        clave = input('Clave: ')
        valor = input('Valor : ')
        diccionario[clave] = valor
    if opcion == 2:
        print(diccionario)
    if opcion == 3:
        break
    else:
        print('Elige una opcion valida.')