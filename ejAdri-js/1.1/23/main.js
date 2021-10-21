// Desarrolla un algoritmo que permita determinar a partir de un número de días, introducido por pantalla, ¿Cuántos años, meses, semanas y días?; constituyen el número de días proporcionado utilizando la estructura Mientras While.
    
let monthsNum = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

let insertDays = prompt('inserte un número de dias.')
let monthsCounter = 1
let months = 0
let contador = 0
let years = 0

for (i = 0; i < insertDays ; i++) {
    if(monthsCounter == 12){
        monthsCounter = 1
    }
    contador ++
    if(contador == monthsNum[monthsCounter]){
        months ++
        if(months%12==0){
            years++
            months = 0
        }
        contador = 0
        monthsCounter++
    }
}

document.write(`
                ${insertDays} days equals: <br>
                ${years} years <br>
                ${months} months <br>
                ${contador} days`)