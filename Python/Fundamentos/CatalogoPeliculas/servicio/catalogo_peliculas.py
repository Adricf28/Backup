import time
import sys
import os
sys.path.append('C:\CursosVS\Python\Fundamentos\CatalogoPeliculas\dominio')
from Pelicula import CPelicula

class CatalogoPeliculas:
    ruta_archivo = 'C:\CursosVS\Python\Fundamentos\CatalogoPeliculas\peliculas.txt'
    
    @staticmethod
    def agregar_pelicula(pelicula_name):
        file = open(CatalogoPeliculas.ruta_archivo, 'a')
        file.write('- ' + pelicula_name + '\n')
        file.close()
        
    @staticmethod
    def listar_peliculas():
        file = open(CatalogoPeliculas.ruta_archivo, 'r')
        print('Lista de peliculas:')
        print(file.read())
        file.close()
        
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print('Eliminando archivo...')
            time.sleep(0.5)
            print(f'El archivo {CatalogoPeliculas.ruta_archivo} ha sido eliminado.')
        except Exception as error:
            print(f'Ha ocurrido el siguiente error: {error}')