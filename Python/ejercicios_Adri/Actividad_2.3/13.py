# 13.- Escriba un programa que permita crear una lista de palabras.
palabras = []
while True:
    opciones = int(input('1- Añadir, 2- Imprimir '))
    if opciones == 1:
        palabras.append(input('Añade una palabra: '))
    elif opciones == 2:
        print(palabras)
        break
    else:
        print('Elige una opcion valida.')