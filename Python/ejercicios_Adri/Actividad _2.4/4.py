# 4.- Crear un programa que borre del diccionario anterior los datos de un alumno pasado por teclado.
diccionario = {}
while True:
    opcion = int(input('1- Añadir alumno y nota, 2- Imprimir, 3- Borrar, 4- Cerrar '))
    if opcion == 1:
        if len(diccionario) == 3:
            print('3 alumnos es el maximo a añadir.')
            break
        alumno = input('Alumno: ')
        nota = float(input('Nota: '))
        if nota < 0 or nota > 10:
            print('Escriba una nota entre 0 y 10.')   # Es posible que me pida la nota otra vez del tiron si le doy una no valida?
        else:
            diccionario[alumno] = str(nota)
    elif opcion == 2:
        print(diccionario)
    elif opcion == 3:
        borrado = input('Que alumno desea borrar?: ')
        for i in diccionario:
            if i == borrado:
                diccionario.pop(i)
            else:
                print('Elige un alumno presente en la lista.')
                break
    elif opcion == 4:
        break
    else:
        print('Elige una opcion valida.')