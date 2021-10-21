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
    dia = facha.getDia()
    mes = facha.getMes()
    if dia < 10:
        print('Faltan', 10 - dia, 'días para cobrar :)')
    elif dia == 10:
        print(' HOY SE ESNINFA')
    elif dia > 10 and dia < mesesNumero.get(mes):
        print(('Faltan {} dias para poder comprar drogas').format(mesesNumero.get(mes) - dia + 10))