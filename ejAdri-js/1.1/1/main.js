// Elaborar un Algoritmo para calcular el área de cualquier triángulo rectángulo y presentar el resultado en pantalla.

let side1 = prompt('Introduce the lenght of one side: ')
let side2 = prompt('Introduce the lenght of the other side: ')

let area = (side1 * side2)/2

document.write(`The area of a triangle with ${side1} and ${side2} long sides is: ${area}`)