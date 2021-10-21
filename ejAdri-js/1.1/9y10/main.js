// Desarrolla un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C respectivamente. El algoritmo debe imprimir cual es el mayor y cuál es el menor. Recuerda constatar que los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de alerta en caso de que se detecte la introducción de valores iguales.

alert('Write 3 different numbers')
let A = parseInt(prompt('Introduce a number: '))
let B = parseInt(prompt('Introduce a number: '))
let C = parseInt(prompt('Introduce a number: '))

if (A != B && A != C && B != C) {
    if (A > B && A > C) {
        if (B > C) {
            document.write(`${A} is the greater number and ${C} is the smaller.`)
        }else {
            document.write(`${A} is the greater number and ${B} is the smaller.`)
        }
    }
    else if (B > A && B > C) {
        if (A > C) {
            document.write(`${B} is the greater number and ${C} is the smaller.`)
        }else {
            document.write(`${B} is the greater number and ${A} is the smaller.`)
        }
    }
    else if (C > A && C > B) {
        if (A > B) {
            document.write(`${C} is the greater number and ${B} is the smaller.`)
        }else {
            document.write(`${C} is the greater number and ${A} is the smaller.`)
        }
    }
    else {
        document.write('r u dumb?')
    }
}else {
    document.write('3 different numbers u dumbass')
}