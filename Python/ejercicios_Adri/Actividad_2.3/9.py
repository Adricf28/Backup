# 9.- Crear un programa que añada un número a la lista: Me pide un número y la posición de la lista y lo añade en dicha posición. 
# (Debemos tener en cuenta que por pantalla debemos decir cuál es el número máximo de la lista)
numeros = [1,2,4,512,3,123,1,2]
numeros.append(int(input('Añade un numero: ')))
print(numeros)
numero = int(input('Elige un numero: '))
for i in numeros:
    if i == numero:
        print('El indice maximo es de ',len(numeros))
        indice = int(input('Indice: '))
        if indice <= len(numeros):
            numeros.insert(int(input('Indice => ')),numero)
            break
        else:
            print('Bobo o que?')
            
print(numeros)