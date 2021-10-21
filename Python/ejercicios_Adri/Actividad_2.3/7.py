# 7.- Crear un programa que añada un número a la lista: Me pide un número de la lista y lo añade al final de la lista.
numeros = [1,2,4,512,3,123,1,2]
numeros.append(int(input('Añade un numero: ')))
print(numeros)
numero = int(input('Elige un numero: '))
for i in numeros:
    if i == numero:
        numeros.append(numero)
        break
    else:
        print('Elige un numero de la lista.')
        break
            
print(numeros)