v1 = float(input('Proporciona un valor: '))
v2 = float(input('Proporciona otro valor: '))
if v1 != v2:
    if v1 < v2:
            print(v1, 'es menor.')
    else:
        print(v2, 'es menor')
else: 
    print('Proporciona dos valores distintos.')