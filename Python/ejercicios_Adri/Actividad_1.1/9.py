A = float(input('Proporciona el primer valor: '))
B = float(input('Proporciona el segundo valor: '))
C = float(input('Proporciona el tercer valor: '))
if A != B != C != A: 
    if A > B and A > C:
        print(A, 'es el numero mayor')
    if B > A and B > C:
        print(B, 'es el numero mayor')
    if C > A and C > B:
        print(C, 'es el numero mayor')
        
    if A < B and A < C:
        print(A, 'es el numero menor')
    if B < A and B < C:
        print(B, 'es el numero menor')
    if C < A and C < B:
        print(C, 'es el numero menor')
else: 
    print('Proporciona tres valores distintos.')