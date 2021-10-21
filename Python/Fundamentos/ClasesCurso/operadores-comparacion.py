a = 20
b = 2

# a es igual a b?
resultado = a == b
print(resultado)

# a es diferente a b?
resultado = a != b
print(resultado)

# a es mayor/menor a b?
resultado = a > b
print(resultado)

# a es mayor/menor o igual a b?
resultado = a >= b
print(resultado)

# a es par? (divisible entre 2)
if a%2 == 0:
    print('Es par')
else:
    print('Es impar')
    
# a es mayor de edad?
edadLimite = 18
edadPersona = 5
if edadPersona >= edadLimite:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')