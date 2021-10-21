# 7.- Dado un mes, devolver la cantidad de días correspondientes. (Pueden introducir el número del mes por ejemplo Enero = 1)

mes = input('Mes: ')
meses = {
    'enero' : 31,
    'febrero' : 28,
    'marzo' : 31,
    'abril' : 30,
    'mayo' : 31,
    'junio' : 30,
    'julio' : 31,
    'agosto' : 31,
    'septiembre' : 30,
    'octubre' : 31,
    'noviembre' : 30,
    'diciembre' : 31
}

# for k,v in meses.items():
#     if mes == k:                                # Forma 1
#         print(v)
print(meses[1])
for x in meses:
    if x == mes:                                  # Forma 2
        print('Dias:', meses.get(x))