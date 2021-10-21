# 15.- Escriba un programa que me pide una cadena, y la elimina de la lista.
palabras = ['Paco', 'Pepe', 'Ozemigue']
while True:
    opciones = int(input('1- Añadir, 2- Imprimir, 3- Apariciones, 4- Eliminar, 5- Cerrar '))
    if opciones == 1:
        palabras.append(input('Añade una palabra: '))
    elif opciones == 2:
        print(palabras)
    elif opciones == 3:
        contador = 0
        palabra = input('Palabra a contar: ')
        for i in palabras:
            if i == palabra:
                contador += 1

        print('La palabra', palabra, 'aparece', contador, 'veces en la lista.')
    elif opciones == 4:
        target = str(input('Escriba una cadena para eliminar: '))
        for i in palabras:
            if i == target:
                palabras.remove(i)
    else:
        break
        
        