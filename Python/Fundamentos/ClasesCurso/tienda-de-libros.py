print('Proporcione los siguientes datos del libro:')
nombre = input('Nombre: ')
id = int(input('ID: '))
precio = float(input('Precio: '))
envioGratuito = input('Indica si el envio es gratuito (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, introduzca True/False'
print('Nombre:', nombre)
print('Id:si', id)
print('Precio:', precio)
print('Envio gratuito?:', envioGratuito)
print(type(envioGratuito))