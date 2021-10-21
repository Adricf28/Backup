# 14.- Escriba un programa que permita contar: Me pide una cadena, y me dice cuántas veces aparece en la lista.
import webbrowser
palabras = []
while True:
    opciones = int(input('1- Añadir, 2- Imprimir, 3- Apariciones '))
    if opciones == 1:
        palabras.append(input('Añade una palabra: '))
    elif opciones == 2:
        print(palabras)
        break
    elif opciones == 3:
        contador = 0
        palabra = input('Alfred hitchcock: ')
        for i in palabras:
            if i == palabra:
                contador += 1

        print('La palabra', palabra, 'aparece', contador, 'veces en la lista.')
    
    else:
        url = 'https://www.youtube.com/watch?v=2mKoW4DtU-s&ab_channel=Dreiker'
        try:
            webbrowser.open_new_tab(url)
            print('Elige una opcion valida.')           
        except webbrowser.Error:
            print("No se ha encontrado chrome.")