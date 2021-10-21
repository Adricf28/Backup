// Desarrolla un algoritmo que realice la sumatoria de los números enteros pares comprendidos entre el 1 y el 100, es decir, 2 + 4 + 6 +…. + 100. El programa deberá imprimir los números en cuestión y finalmente su sumatoria.

let counter = 0
let totalNum = []

for (i = 2; i < 101; i+=2) {
    counter = counter + i
    totalNum.push(counter)
}

console.log(totalNum);
console.log(totalNum.length);