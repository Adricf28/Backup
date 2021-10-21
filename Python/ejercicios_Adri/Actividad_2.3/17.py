# 16.- Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de mayor a menor.
loteria = []
while True:
    opcion = int(input('1- Añadir, 2- Mostrar, 3- Cerrar '))
    if opcion == 1:
        loteria.append(int(input('Numeros ganadores: ')))
    elif opcion == 2:
        loteria.sort(reverse=True)
        print(loteria)
    elif opcion == 3:
        break
    else:
        print('Elige una opcion valida.')