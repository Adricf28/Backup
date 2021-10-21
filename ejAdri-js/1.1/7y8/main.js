// Desarrolla un algoritmo que permita leer dos valores distintos, determinar cuál de los dos valores es el mayor y escribirlo.
// Realizar un algoritmo que permita leer dos valores, determinar cuál de los dos valores es el menor y escríbelo.

let num1 = parseInt(prompt('Write a number: '))
let num2 = parseInt(prompt('Write another number: '))

if (num1 > num2) {
    document.write(`${num1} is greater than ${num2}`)
}
else if (num1 < num2) {
    document.write(`${num2} is greater than ${num1}`)
}
else if (num1 == num2) {
    document.write(`${num1} and ${num2} are equal`)
}
else {
    document.write('r u dumb?')
}