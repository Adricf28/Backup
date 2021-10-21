// Realice un algoritmo que determine los veinte primeros números, ¿Cuáles son múltiplos de 2?.

let pair = []

for (i = 1; i < 21; i++) {
    if (i % 2 == 0) {
        pair.push(i)
    }
}

console.log(pair);