contactos = []
while True:
    pregunta = int(input('1- Añadir contacto , 2- Borrar contacto , 3- Cerrar \n'))
    if pregunta == 1:
        nombre = str(input('Nombre del contacto: '))
        telefono = int(input('Numero del contacto: '))
        contacto = [nombre, telefono]
        contactos.append(contacto)
    elif pregunta == 2:
        if len(contactos) > 0:
            posicion = 0
            for i in contactos:
                posicion += 1
                print(posicion, i[0], i[1])
                borrado = int(input('Contacto a borrar: '))
                print('El contacto borrado es: ', contactos[borrado-1][0])
                contactos.pop(borrado-1)
            else:
                print('No hay contactos')
    elif pregunta == 3:
        break