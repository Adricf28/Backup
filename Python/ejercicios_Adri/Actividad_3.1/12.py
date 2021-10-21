# Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días. (La fecha se debe introducir de la siguiente forma DD/MM/YYYY)

from claseFecha import Facha

from datetime import date

fecha1 = Facha(int(input('Dia: ')), int(input('Mes: ')), int(input('Año: ')))
fecha2 = Facha(int(input('Dia: ')), int(input('Mes: ')), int(input('Año: ')))

date1= date(fecha1.getAño(),fecha1.getMes(),fecha1.getDia())
date2= date(fecha2.getAño(),fecha2.getMes(),fecha2.getDia())
diference = date2 - date1
print(str(diference.days))