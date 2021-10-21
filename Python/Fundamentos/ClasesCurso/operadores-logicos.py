# and (se cumplen ambas variables)
a = 3
valorMinimo = 0
valorMaximo = 5
enRango = a >= valorMinimo and a <= valorMaximo
if enRango:
    print('En rango')
else:
    print('Fuera de rango')

# or (se cumple al menos una variable)
vacaciones = True
diaDescanso = True
if vacaciones or diaDescanso:
    print('Puedes ir al parque')
else:
    print('Tienes deberes que hacer')
    
# not (invierte expresiones bulianas)
vacaciones = False
diaDescanso = True
if not(vacaciones or diaDescanso):
    print('Tienes deberes que hacer')
else:
    print('Puedes salir')
