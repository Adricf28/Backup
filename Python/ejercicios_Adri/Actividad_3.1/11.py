# 11.- Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha. (La fecha se debe introducir de la siguiente forma DD/MM/YYYY)

from claseFecha import Facha

mesesNumero = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

while True:
    facha = Facha(int(input('Dia: ')), int(input('Mes: ')), int(input('Año: ')))
    dias = (mesesNumero.get(facha.getMes()))-facha.getDia()
    diasRestantes = dias
    for mes in mesesNumero:
        if mes > facha.getMes():
            diasRestantes+=mesesNumero.get(mes)
    print('Faltan', diasRestantes, 'dias para que acabe el año.')
    
    print('Llevamos', 365 - diasRestantes, 'dias este año.')
    
    
    