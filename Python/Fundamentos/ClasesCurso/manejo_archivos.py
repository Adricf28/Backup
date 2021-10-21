try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Agregando info al archivo... \n')
    archivo.write('Adios.')
except Exception as e:
    print(e)
finally:
    archivo.close()
    
