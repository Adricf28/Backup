# 8.- Dada una fecha (día, mes, año), indicar si es válida o no. (La fecha se debe introducir de la siguiente forma DD/MM/YYYY)

class Facha:
    
    def __init__(self, dia, mes, año):
        if dia in range(1,32):
            self.dia = dia
            if mes in range(1,13):
                self.mes = mes
                if año in range(1900,2030):
                    self.año = año
                else:
                    print('Año mal introducido')
            else:
                print('Mes mal introducido')
        else:
            print('Dia mal introducido')
            
    @staticmethod
    def horoscopo(fecha):
        dia = fecha.getDia()
        mes = fecha.getMes()

        if dia >= 21 and mes == 3 or dia <= 20 and mes == 4 :
            print("Eres Aries ")
        if dia >= 21 and mes == 4 or dia <= 20 and mes == 5 :
            print("Eres Tauro ")
        if dia >= 21 and mes == 5 or dia <= 21 and mes == 6 :
            print("Eres Géminis ")
        if dia >= 22 and mes == 6 or dia <= 23 and mes == 7 :
            print("Eres Cancer ")
        if dia >= 24 and mes == 7 or dia <= 23 and mes ==8 :
            print("Eres Leo ")
        if dia >= 24 and mes == 8 or dia <= 22 and mes == 9 :
            print("Eres Virgo ")
        if dia >= 24 and mes == 9 or dia <= 22 and mes == 10 :
            print("Eres Libra")
        if dia >= 23 and mes == 10 or dia <= 22 and mes == 11 :
            print("Eres Escorpio ")
        if dia >= 23 and mes == 11 or dia <= 21 and mes ==12 :
            print("Eres Sagitario ")
        if dia >= 22 and mes == 12 or dia <= 20 and mes == 1 :
            print("Eres Capricornio ")
        if dia >= 21 and mes == 1 or dia <= 19 and mes == 2 :
            print("Eres Acuario ")
        if dia >= 20 and mes == 2 or dia <= 20 and mes == 3 :
            print("Eres Piscis ")   
    
                
        
            
    def getDia(self):
        return self.dia
    def getMes(self):
        return self.mes
    def getAño(self):
        return self.año
        
    def __str__(self):
        return 'Dia : ' + str(self.dia) + '\n' + 'Mes: ' + str(self.mes) + '\n' + 'Año: ' + str(self.año)
