// Desarrolla un algoritmo que permita leer dos números y ordenarlos de menor a mayor, si es el caso.

let num1 = parseInt(prompt('Write a number'))
let num2 = parseInt(prompt('Write a number'))
let numbers = [num1,num2]
numbers.sort(function(a,b){return a-b})
document.write(`Numeros ordenados de menor a mayor: ${numbers}.`)