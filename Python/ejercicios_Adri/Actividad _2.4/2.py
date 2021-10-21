# 2.- Copia los elementos de un diccionario a otro y muestra sus elementos por la pantalla
diccionario1 = {
    'BOE': 'Boletin Oficial del Estado',
    'EEUU': 'Estados Unidos',
    'LATAM': 'Latino America'    
}
diccionario2 = {}

elemento = input('Elige una clave a copiar: ')
diccionario2[elemento] = diccionario1[elemento]
print(diccionario1)
print(diccionario2)
print(len(diccionario1))