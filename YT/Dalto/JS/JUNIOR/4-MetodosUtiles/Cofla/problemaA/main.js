class Calcular {
    sumar(num1,num2){
        return num1 + num2
    }
    restar(num1,num2){
        return num1 - num2
    }
    multiplicar(num1,num2){
        return num1 * num2
    }
    dividir(num1,num2){
        return num1 / num2
    }
    elevar(num1,num2){
        return num1 ** num2
    }
    raizCuadrada(num1){
        return Math.sqrt(num1)
    }
    raizCubica(num1){
        return Math.cbrt(num1)
    }
}

const operacion = new Calcular()
let alerta = alert("A continuacion, elige la operacion que quieres realizar")
let eleccion = prompt("1- Suma, 2- Resta, 3- Multiplicacion, 4- Division, 5- Potencia, 6- Raiz Cuadrada, 7- Raiz Cubica")

if (eleccion == 1) {
    let n1 = parseFloat(prompt("Primer numero a sumar"))
    let n2 = parseFloat(prompt("Segundo numero a sumar"))
    document.write(`${n1} + ${n2} = <b>${operacion.sumar(n1,n2)}</b>`)
}
else if (eleccion == 2) {
    let n1 = parseFloat(prompt("Primer numero a restar"))
    let n2 = parseFloat(prompt("Segundo numero a restar"))
    document.write(`${n1} - ${n2} = <b>${operacion.restar(n1,n2)}</b>`)
}
else if (eleccion == 3) {
    let n1 = parseFloat(prompt("Primer numero a multiplicar"))
    let n2 = parseFloat(prompt("Segundo numero a multiplicar"))
    document.write(`${n1} * ${n2} = <b>${operacion.multiplicar(n1,n2)}</b>`)
}
else if (eleccion == 4) {
    let n1 = parseFloat(prompt("Primer numero a dividir"))
    let n2 = parseFloat(prompt("Segundo numero a dividir"))
    document.write(`${n1} / ${n2} = <b>${operacion.dividir(n1,n2)}</b>`)
}
else if (eleccion == 5) {
    let n1 = parseFloat(prompt("Primer numero a elevar"))
    let n2 = parseFloat(prompt("Segundo numero a elevar"))
    document.write(`${n1} ** ${n2} = <b>${operacion.elevar(n1,n2)}</b>`)
}
else if (eleccion == 6) {
    let n1 = parseFloat(prompt("Introduce un numero"))
    document.write(`La raiz cuadrada de ${n1} = <b>${operacion.raizCuadrada(n1)}</b>`)
}
else if (eleccion == 7) {
    let n1 = parseInt(prompt("Introduce un numero"))
    document.write(`La raiz cubica de ${n1} = <b>${operacion.raizCubica(n1)}</b>`)
}