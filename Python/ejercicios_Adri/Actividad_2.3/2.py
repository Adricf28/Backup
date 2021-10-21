# 2.- Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
lista = [] 
lista.append(input('Introduce uuna polla: '))
lista.append(input('Introduce uuna polla: '))
lista.append(input('Introduce uuna polla: '))
print('Lista: ', lista)

lista.reverse()
listacopia = []
for i in lista:
    listacopia.append(i)
print('Copia lista: ', listacopia)
    