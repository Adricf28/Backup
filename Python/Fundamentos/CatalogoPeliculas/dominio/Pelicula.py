class CPelicula:
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return f'El nombre de la pelicula es: {self.__name}'
    def get_nombre(self):
        return self.__name
    def set_name(self, n):
        self.__name = n