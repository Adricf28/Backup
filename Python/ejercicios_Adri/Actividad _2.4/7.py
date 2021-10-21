# 7.- Visualizar los valores del diccionario del ejercicio 1.
diccionario = {}
while True:
    opcion = int(input('1- Añadir, 2- Listar, 3- Listar solo claves, 4- Listar solo valores, 5- Cerrar '))
    if opcion == 1:
        clave = input('Clave: ')
        valor = input('Valor : ')
        diccionario[clave] = valor
    elif opcion == 2:
        print(diccionario)
    elif opcion == 3:
        for i in diccionario:
            print(i)
    elif opcion == 4:
        for i in diccionario.values():
            print(i)
    elif opcion == 5:
        break
    else:
        print('Elige una opcion valida.')