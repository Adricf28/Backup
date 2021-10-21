# 3.- Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno se entiende que están comprendidas entre 0 y 10. Guardarlas en una lista y ordenarlas de mayor a menor.
notas = []
notas.append(float(input('Nota 1: ')))
notas.append(float(input('Nota 2: ')))
notas.append(float(input('Nota 3: ')))
notas.append(float(input('Nota 4: ')))
notas.append(float(input('Nota 5: ')))
notasBien = []
for i in notas:
    if i in range(11):
        notasBien.append(i)
    else:
        pass
        print('La nota introducida ', i , 'no es valida.')
notasBien.sort(reverse=True)
print(notasBien)