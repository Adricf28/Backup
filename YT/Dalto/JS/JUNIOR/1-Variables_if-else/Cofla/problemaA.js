const agua = 0.6
const crema = 1
const heladix = 1.6
const heladovich = 1.7
const helardo = 1.8
const confites = 2.9
const cuartoKG = 2.9

let name1 = prompt('¿Cómo te llamas?')
let money1 = parseInt(prompt(`¿Cuánto dinero tienes, ${name1}?`))

if (money1 >= 0.6 && money1 < 1) {
    alert(`El helado mas caro que puedes comprar es el de agua, y te sobran ${money1 - 0.6}`)
}
else if (money1 >= 1 && money1 < 1.6) {
    alert(`El helado mas caro que puedes comprar es el de crema, y te sobran ${money1 - 1}`)
}
else if (money1 >= 1.6 && money1 < 1.7) {
    alert(`El helado mas caro que puedes comprar es el de heladix, y te sobran ${money1 - 1.6}`)
}
else if (money1 >= 1.7 && money1 < 1.8) {
    alert(`El helado mas caro que puedes comprar es el de heladovich, y te sobran ${money1 - 1.7}`)
}
else if (money1 >= 1.8 && money1 < 2.9) {
    alert(`El helado mas caro que puedes comprar es el de helardo, y te sobran ${money1 - 1.8}`)
}
else if (money1 >= 2.9) {
    alert(`El helado mas caro que puedes comprar es el de confites o un cuarto de kg, y te sobran ${money1 - 2.9}`)
}
else {
    alert(`Casi crack`)
}