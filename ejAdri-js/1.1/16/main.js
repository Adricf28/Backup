// Desarrolla un algoritmo que permita convertir calificaciones numéricas, según la siguiente tabla: A = 19 y 20, B =16, 17 y 18, C = 13, 14 y 15, D = 10, 11 y 12, E = 1 hasta el 9. Se asume que la nota está comprendida entre 1 y 20.

function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}

let A = [19,20]
let B = [16,17,18]
let C = [13,14,15]
let D = [10,11,12]
let E = [9,8,7,6,5,4,3,2,1]

let points = parseInt(prompt('How many points did u get?'))

if (isNumber(points)) {
    if (A.includes(points)) {
        document.write('Congratulations, you got an A calification.')
    }
    else if (B.includes(points)) {
        document.write('Good job, you got a B calification.')
    }
    else if (C.includes(points)) {
        document.write('Could have done better, but still approved. You got a C calification.')
    }
    else if (D.includes(points)) {
        document.write('On the edge, you should study more. D calification.')
    }
    else if (E.includes(points)) {
        document.write('Disgusting, you are not gonna pass this year if you keep like this. E calification.')
    }
}else {
    document.write('dumb or what?')
}