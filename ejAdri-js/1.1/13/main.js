// Desarrolla un algoritmo que realice la sumatoria de los números enteros múltiplos de 5, comprendidos entre el 1 y el 100, es decir, 5 + 10 + 15 +…. + 100. El programa deberá imprimir los números en cuestión y finalmente su sumatoria.

let counter = 5
let totalNum = []

for (i = 5; i < 101; i+=5) {
    counter = counter + i
    totalNum.push(counter)
}

console.log(totalNum);
console.log(totalNum.length);