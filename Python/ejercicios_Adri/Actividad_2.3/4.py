# 4.- Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
lista1 = []
lista2 = []
lista3 = lista1 + lista2

# lista1.append(int(input('Introduzca un valor: ')))
# lista1.append(int(input('Introduzca un valor: ')))
# lista1.append(int(input('Introduzca un valor: ')))
# lista1.append(int(input('Introduzca un valor: ')))
# lista1.append(int(input('Introduzca un valor: ')))

# lista2.append(int(input('Introduzca un valor: ')))
# lista2.append(int(input('Introduzca un valor: ')))
# lista2.append(int(input('Introduzca un valor: ')))
# lista2.append(int(input('Introduzca un valor: ')))
# lista2.append(int(input('Introduzca un valor: ')))

for i in range(1,3):
    if i == 1:
        for j in range(5):
            lista1.append(int(input('Introduzca un valor: ')))
    else:
        for j in range(5):
            lista2.append(int(input('Introduzca un valor: ')))
        
# for i in lista1:
#     lista3.append(i)  
# for i in lista2:
#     lista3.append(i)

print(lista1)
print(lista2)
print(lista3)
