A = float(input('Proporciona el primer valor: '))
B = float(input('Proporciona el segundo valor: '))
C = float(input('Proporciona el tercer valor: '))
D = float(input('Proporciona el cuarto valor: '))
numeros = [A,B,C,D]
n = sorted(numeros)
print('El numero mayor es: ', n[-1])              # Forma 1
print('El numero menor es: ', n[0])      
numeros.sort()
print('El numero mayor es ', numeros[-1])         # Forma 2
print('El numero menor' , numeros[0])

# if A != B != C != A and D != A and D != B and D != C: 
#     if A > B and A > C and A > D:
#         print(A, 'es el numero mayor')
#     if B > A and B > C and B > D:
#         print(B, 'es el numero mayor')                         XDXDXDXDXDXDXDXD
#     if C > A and C > B and C > D:
#         print(C, 'es el numero mayor')
#     if D > A and D > B and D > C:                              XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
#         print(D, 'es el numero mayor')      
        
#     if A < B and A < C and A < D:
#         print(A, 'es el numero menor')
#     if B < A and B < C and B < D:                                    KEKW
#         print(B, 'es el numero menor')
#     if C < A and C < B and C < D:
#         print(C, 'es el numero menor')
#     if D < A and D < B and D < C:
#         print(D, 'es el numero menor')                                      xdddddddddddddd
# else: 
#     print('Proporciona cuatro valores distintos.')