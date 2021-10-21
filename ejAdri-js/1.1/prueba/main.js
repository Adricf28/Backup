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

// alert("Elige opcion en el siguiente mensaje.")
// let opcion = prompt("1- Pasar dias a años. 2- Pasar años a dias")

let monthsCounter = 1
let months = 0
let contador = 0
let years = 0

// if (opcion == 1) {
    let insertDays = prompt('Inserte un número de dias')
    for (i = 0; i < insertDays ; i++) {
        if (years%4==0){
            monthsNum[2] = 29 
        }else {
            monthsNum[2] = 28
        }

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
                <ul>
                    <li><b>${insertDays} days equals:</b></li>
                    <li>${years} years</li>
                    <li>${months} months</li>
                    <li>${contador} days</li>
                </ul>`)
// } 
// else if (opcion == 2) {
//     let insertYears = prompt("Inserte un numero de años")
//     let dias = insertYears * 365
//     document.write(`
//                 <ul>
//                     <li><b>${insertYears} years equals:</b> ${dias} days.</li></ul>`)
// }
// else {
//     document.write("Eres tonto?")
// }