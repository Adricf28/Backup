# 9.- Dada una fecha, indicar los días que faltan hasta fin de mes. (La fecha se debe introducir de la siguiente forma DD/MM/YYYY)
from claseFecha import Facha


mesesTexto = {
    '1' : 'enero',
    '2' : 'febrero',
    '3' : 'marzo',
    '4' : 'abril',
    '5' : 'mayo',
    '6' : 'junio',
    '7' : 'julio',
    '8' : 'agosto',
    '9' : 'septiembre',
    '10' : 'octubre',
    '11' : 'noviembre',
    '12' : 'diciembre'
}

mesesNumero = {
    '1' : 31,
    '2' : 28,
    '3' : 31,
    '4' : 30,
    '5' : 31,
    '6' : 30,
    '7' : 31,
    '8' : 31,
    '9' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31
}

while True:
    fecha1 = Facha(int(input('Dia: ')), int(input('Mes: ')), int(input('Año: ')))
    for mes,dias in mesesNumero.items():
        if int(mes) == fecha1.getMes():
            for mesTraductor in mesesTexto:
                if mesTraductor == mes:
                     print('Faltan', dias-fecha1.getDia(), 'dias para que empiece', mesesTexto.get(str(int(mesTraductor)+1)))