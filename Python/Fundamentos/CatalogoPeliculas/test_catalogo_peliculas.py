import time
import sys
sys.path.append('C:\CursosVS\Python\Fundamentos\CatalogoPeliculas\dominio')
sys.path.append('C:\CursosVS\Python\Fundamentos\CatalogoPeliculas\servicio')
from Pelicula import CPelicula
from catalogo_peliculas import CatalogoPeliculas

while True:
    opcion = int(input('Elige una opcion: \n 1- Agregar pelicula \n 2- Listar peliculas \n 3- Eliminar archivo \n 4- Cerrar \n'))
    time.sleep(0.4)
    if opcion == 1:
        movie_name = input('Nombre de la pelicula: ')
        pelicula = CPelicula(movie_name)
        CatalogoPeliculas.agregar_pelicula(movie_name)
        time.sleep(0.2)
    elif opcion == 2:
        CatalogoPeliculas.listar_peliculas()
        time.sleep(1)
    elif opcion == 3:
        CatalogoPeliculas.eliminar()
        time.sleep(1)
    elif opcion == 4:
        break
    else:
        print('Elige una opcion valida.')
        time.sleep(0.7)