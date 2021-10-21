# 6.- Crear un programa que borre de la lista anterior los datos de un alumno pasado por teclado. (Si están repetidos los nombres que borre el primero).
alumnos = []
while True:
    opcion = int(input('1-Añadir, 2-Listar, 3-Borrar '))
    if opcion == 1:
        nombre = input('Nombre: ')
        edad = int(input('Edad: '))
        alumno = [nombre,edad]
        alumnos.append(alumno)
    elif opcion == 2:
        print(alumnos)
        for i in alumnos :
            print('Nombre : ', i[0], 'Edad : ', i[1])
    elif opcion == 3:
         palpozo = input('Nombre a eliminar: ')
         for i in alumnos:
             if i[0] == palpozo:
                 alumnos.remove(i)
    else:
        break



