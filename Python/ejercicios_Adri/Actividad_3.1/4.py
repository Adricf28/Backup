# 4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ 
# y si es mayor de 18 años, 10€.

while True:
    opcion = int(input('1- Comprobar cliente, 2- Cerrar '))
    if opcion == 1:
        edad = int(input('Edad: '))
        entrada = 0
        if edad < 4 and edad > 0:
            entrada = 0
            print('La entrada para clientes de entre 0 y 4 años es gratis.')
        elif edad >= 4 and edad <= 18:
            entrada = 5
            print('La entrada para personas de entre 4 y 18 años es de ' + str(entrada) + '$')
        elif edad > 18 and edad < 110:
            entrada = 10
            print('La entrada para clientes mayores de 18 años es de ' + str(entrada) + '$')
    elif opcion == 2:
        break
    else:
        print('Elige una opcion valida.')
