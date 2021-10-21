# 12.- Crear un programa que te pide un número y te dice cuántas apariciones hay en la lista.
numeros = [12,2,31,12,23,4,2,12]

aparecedor = int(input('Dime el aparecedor que apareceda en la lista '))

contador = 0
for i in numeros:
    if i == aparecedor:
        contador += 1
print('El numeros', aparecedor, 'aparece', contador, ' veces.')