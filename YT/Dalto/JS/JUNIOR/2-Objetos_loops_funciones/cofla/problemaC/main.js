// Crear calculadora

const sumar = (n1,n2) => {return parseInt(n1) + parseInt(n2)}
const restar = (n1,n2) => {return parseInt(n1) - parseInt(n2)}
const multiplicar = (n1,n2) => {return parseInt(n1) * parseInt(n2)}
const dividir = (n1,n2) => {return parseInt(n1) / parseInt(n2)}

let operacion = prompt('Que operacion quieres realizar?: 1- Suma, 2- Resta, 3- Multiplicacion, 4- Division')

if (operacion == 1) {
    let num1 = prompt('Primer numero para sumar: ')
    let num2 = prompt('Segundo numero para sumar: ')
    document.write(`${num1} + ${num2} = ${sumar(num1,num2)}`)
}

else if (operacion == 2) {
    let num1 = prompt('Primer numero para restar: ')
    let num2 = prompt('Segundo numero para restar: ')
    document.write(`${num1} - ${num2} = ${restar(num1,num2)}`)
}

else if (operacion == 3) {
    let num1 = prompt('Primer numero para multiplicar: ')
    let num2 = prompt('Segundo numero para multiplicar: ')
    document.write(`${num1} * ${num2} = ${multiplicar(num1,num2)}`)
}

else if (operacion == 4) {
    let num1 = prompt('Primer numero para dividir: ')
    let num2 = prompt('Segundo numero para dividir: ')
    document.write(`${num1} / ${num2} = ${dividir(num1,num2)}`)
}
else {
    document.write('Bobo o que?')
}