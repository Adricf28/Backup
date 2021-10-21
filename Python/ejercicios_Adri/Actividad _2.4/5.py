# 5.- Crear un programa que muestre la longitud del diccionario: te muestra el número de elementos del diccionario.
diccionario = {}
while True:
    opcion = int(input('1- Añadir alumno y nota, 2- Imprimir, 3- Cerrar '))
    if opcion == 1:
        if len(diccionario) == 3:
            print('3 alumnos es el maximo a añadir.')
            break
        alumno = input('Alumno: ')
        nota = float(input('Nota: '))
        if nota < 0 or nota > 10:
            print('Escriba una nota entre 0 y 10.')
        else:
            diccionario[alumno] = str(nota)
    elif opcion == 2:
        print(diccionario)
    elif opcion == 3:
        break
    else:
        print('Elige una opcion valida.')
        
print('El diccionario tiene una longitud de', len(diccionario))