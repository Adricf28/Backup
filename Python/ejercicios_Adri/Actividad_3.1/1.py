# 1.- Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
tributan = []
noTributan = []
while True:
    opcion = int(input('1- Añadir usuario, 2- Listar, 3- Cerrar '))
    if opcion == 1:
        usuario = input('Escriba su nombre: ')
        edad = int(input('Edad: '))
        ingresos = int(input('Ingresos mensuales: '))
        if edad > 16 and ingresos >= 1000:
            tributan.append(usuario)
            print(usuario, 'debe tributar.')
        else:
            noTributan.append(usuario)
            print(usuario, 'no debe tributar.')
    elif opcion == 2:
        opciones = int(input('Elige qué listar: 1- Tributantes, 2- No tributantes '))
        if opciones == 1:
            print(tributan)
        elif opciones == 2:
            print(noTributan)
        else: 
            print('Elige una opcion valida')
    elif opcion == 3:
        break
    else: 
        print('Elige una opcion valida')
    