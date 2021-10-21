// Desarrolla un algoritmo que lea cuatro números diferentes y a continuación imprima el mayor de los cuatro números introducidos y también el menor de ellos.

alert('Introduce 4 different numbers')
let num1 = parseInt(prompt('Write a number: '))
let num2 = parseInt(prompt('Write a number: '))
let num3 = parseInt(prompt('Write a number: '))
let num4 = parseInt(prompt('Write a number: '))


if (num1 != num2 && num1 != num3 && num1 != num4 && num2 != num3 && num2 != num4 && num3 != num4) {
    let numbers = [num1,num2,num3,num4]
    numbers.sort(function(a,b){return b-a})
    document.write(`${numbers[0]} is the greater number and ${numbers[3]} is the smallest number.`)
}else {
    document.write('Introduce 4 different number u nerd')
}