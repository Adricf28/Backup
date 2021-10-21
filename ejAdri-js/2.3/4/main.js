// Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

let lista1 = []
let lista2 = []

for (i = 0; i < 5; i++){
    let num = parseFloat(prompt("Introduce a number:"))
    lista1.push(num)
}
for (i = 0; i < 5; i++){
    let num = parseFloat(prompt("Introduce a number:"))
    lista2.push(num)
}

let lista3 = lista1.concat(lista2)

if (lista1.includes(NaN) || lista2.includes(NaN)) {
    document.write("Introduce solo numeros gilipollas")
} else {
    document.write(`Lista 1: ${lista1}<br><br>Lista 2: ${lista2}<br><br>Lista 3: ${lista3}`)
}