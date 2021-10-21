try:
    # archivo = open('C:\\CursosVS\\Python\\Fundamentos\\prueba.txt', 'r') # Se puede acceder asi tambien
    archivo = open('prueba.txt', 'r')
    # print(archivo.read())
    
    # print(archivo.read(5)) # Leer solo cierta cantidad de caracteres
    # print(archivo.read(3)) # Si se vuelve a ejecutar, lee desde donde termino la vez anterior
    
    # print(archivo.readline()) # Leer una sola linea
    # print(archivo.readline()) # Si se vuelve a ejecutar, lee desde donde termino la vez anterior
    
    # for linea in archivo:
    #     print(linea) # Itera linea a linea
    
    # print(archivo.readlines()) # Imprime una lista con todas las lineas del archivo
    # print(archivo.readlines()[2]) # Puedes elegir que linea imprimir
    
    archivo2 = open('copia.txt', 'w')
    # archivo2 = open('copia.txt', 'a') # Con a hace un append, de esta manera no se borra todo cada vez que se ejecute el programa
    archivo2.write(archivo.read()) # Copiar todo un archivo en otro
except Exception as e:
    print(e)
finally:    
    archivo.close()
    archivo2.close()