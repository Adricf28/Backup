# 5.- Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno y se almacene en una lista de forma que cada nombre y edad estén en una sublista por ejemplo:

 #lista = [[“Pedro”,27], [“Juan”,25]]
 
# name = input('Insert name: ')
# age = input('Insert age: ')
# x = [name, age]
# name1 = input('Insert name: ')                  # Forma 1
# age1 = input('Insert age: ')
# x1 = [name1, age1]
# lista = []

# lista.append(x)
# lista.append(x1)
# print(lista)


alumnos = []
while True:
    opcion = int(input('1-Añadir , 2-Listar'))
    if opcion == 1:
        nombre = input('Nombre: ')
        edad = int(input('Edad: '))
        alumno = [nombre,edad]
        alumnos.append(alumno)
    elif opcion == 2:
        print(alumnos)
        for i in alumnos :
            print('Nombre : ', i[0], 'Edad : ', i[1])
    else:
        break
