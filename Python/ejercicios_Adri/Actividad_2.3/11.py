# 11.- Crear un programa que elimine el último número: Muestra el último número de la lista y lo borra.
numeros = [1,2,4,512,3,123,1,2]
numeros.append(int(input('Añade un numero: ')))
print(numeros)
numero = int(input('Elige un numero: '))
buliano = True
while buliano:
    for i in numeros:
        if i == numero:
            print('El indice maximo es de ',len(numeros))
            indice = int(input('Indice: '))
            if indice <= len(numeros):
                numeros.insert(indice, numero)
                buliano = False
                break
            else:
                print('Bobo o que?')
            
print(numeros)
print('Ultimo numero de la lista: ', numeros[-1])
numeros.pop()
print(numeros)