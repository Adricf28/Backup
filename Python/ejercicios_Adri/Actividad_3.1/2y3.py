# 2.- En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# 3.- Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

employees =[]
while True:
    
    option = int (input("1-Añadir Empleado , 2-Ver puntuación de un empleado , 3-Ver ingresos finales de un empleado "))
    
    if option == 1 :
        name = input('Name of the employee ')
        score = float(input('Score of the employee (0.0,0.2,0.4,0.6,0.8,1.0) '))
        base_payroll = 2400
        employee = [name , score, base_payroll]
        employees.append(employee)
    if option == 2:
        print(employees)
        select = input('Choose one name of the list ')
        for i in employees:
            if i[0] == select:
                print(i[0] , 'has a score of ' , i[1])
    if option == 3:
        print(employees)
        select = input('Choose one name of the list ')
        for i in employees:
                if i[0] == select:
                    print(i[0] , 'has a month payroll of ' , (i[2] * i[1]))
        