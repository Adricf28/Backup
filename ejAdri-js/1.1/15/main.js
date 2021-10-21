// Desarrolla un algoritmo que lea los primeros 300 números enteros y determine cuántos de ellos son impares; al final deberá indicar su sumatoria.

let odd = []

for (i = 0; i < 300; i++) {
    if (i % 2 != 0) {
        console.log(i);
        odd.push(i)
    }
}

console.log(odd);
console.log(odd.length);