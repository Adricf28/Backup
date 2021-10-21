valor = float(input('Proporciona un valor entre 0 y 10: '))
calificacion = None
if valor >= 0 and valor < 6:
    calificacion = 'F'
elif valor >= 6 and valor < 7:
    calificacion = 'D'
elif valor >= 7 and valor < 8:
    calificacion = 'C'
elif valor >= 8 and valor < 9:
    calificacion = 'B'
elif valor >= 9 and valor <= 10:
    calificacion = 'A'
elif valor < 0 or valor > 10:
    print('Valor incorrecto')
    
if valor >= 0 and valor <= 10:
    print('Su calificacion es:', calificacion)