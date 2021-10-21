condicion = False

print('Condicion verdadera') if condicion else print('Condicion falsa')

if condicion == True:
    print('La condicion es verdadera')
elif condicion == False:
    print('La condicion es falsa')
else:
    print('Condicion no reconocida')
    
numero = int(input('Proporciona un numero entre 1 y 3: '))
if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'Valor fuera de rango'
print('Numero proporcionado:', numeroTexto)
    