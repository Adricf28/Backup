// console.log('Hola Mundo')

//Tipos de datos
    // Null = None
    // Undefined = Variable aun sin definir


//Definicion de variables
    // var = Va a la raiz del archivo, forma antigua de definir variables
    // let define variables que se pueden redefinir mas adelante
    // const define constantes, por lo tanto no se pueden cambiar

// var MiPrimeraVariable = 'nonononono'

let MPV = 'sisisisiis'

MPV = 'changing var'

let miBoolean = true
let miBoolean2 = false

let miNumero = 1
let miNumero2 = 2
let miNumero3 = -3


// let undef // Variable indefinida, sin darle valor con un igual

let nulo = null

// Objeto = Agrupacion de datos con sentido entre sí
const miObjeto = {
    num1: 12,
    str1: 'Armondiga',
    bool1: true,
}

// Arreglo = lista
const arrVacio = []
const arreglo = [1,2,'hola', 'mundo', miObjeto]

// .push inserta items a los arrays/listas
arrVacio.push(5)
arrVacio.push(3)
arrVacio.push(1)
arrVacio.push('hola')
arrVacio.push(MPV)


// OPERACIONES BASICAS
const suma = 1 + 2
const restar = 3 - 1
const multiplicar = 1 * 1
const dividir = 12 / 3
const modulo = 10 % 3

let num = 5
// num++  num++ suma uno a la variable num
// num++  para sumar varios hay que pegarlo varias veces
// num++

// num--  num-- igual pero para restar
// num--
// num--

num += 3
num -= 5
num *= 2
num /= 3

// COMPARACIONES
const res1 = 5 === '5' // el === compara si son estrictamente identicos
const res2 = 5 == '5'// el == compara si son identicos, aunque uno sea str

const res3 = 5 !== '5' // !== compara si son estrictamente desiguales
const res4 = 5 != '5' // != compara si son desiguales, aunque uno sea str

const res5 = 5 < 6
const res6 = 5 > 6

const res7 = 7 <= 6
const res8 = 5 >= 6


// OR / AND / NOT
// or se escribe ||  and se escribe &&   not se escribe !
const resOR = true || false

const resAND = true && false

const resNOT = !true


// IF
// const edad = 19
// if (edad > 5 && edad < 18) {
//     console.log('Edad permitida');
// } else {
//     console.log('');
// }

// WHILE
let x = 6
while (x < 5) {
    console.log(x);
    x++
}

// SWITCH ejecuta un caso depende de el valor que le pases
// let opcion = 20
// switch (opcion) {
//     case 1: {
//         console.log('Caso 1');
//         break;
//     }
//     case 2: {
//         console.log('Caso 2');
//         break;
//     }
//     case 3:
//         console.log('Caso 3');
//         break;

//     default:  // default se ejecuta si no es ninguno de los otros casos
//         console.log('');
//         break;
// }

// FOR
// for (let i = 0; i<10; i++) {
//     console.log(i);
// }


// FUNCIONES
// function iterar(arg1) {

//     for (let i = 0; i < arg1.length; i++) {
//         console.log(arg1[i]);
//     }   
// }

// const nums = [1,2,'hola',4,5]
// const nombres = ['Pedro', 'Juan', 'Paco', 'Monica']
// iterar(nums)
// iterar(nombres)

function sumar(a, b) {
    return a + b;
}

const resSuma1 = sumar(1,2)
const resSuma2 = sumar(5,6)
const resSuma3 = sumar(resSuma1, resSuma2)

// console.log('Resultado:', resSuma3);

function sumar2(a, b, cb) {
    const r = a+b
    cb(r)
}

function callback(result) {
    console.log('Resultado:', result);
}
// sumar2(2,3, callback)


// FAT ARROW FUNCTION
const faf = (a,b) => a+b

const faf2 = (a,b) => {
    return 'Suma: ' + a+b
}
const r = faf2(1,2)

sumar2(2,3, function (r) {
    console.log('Funcion anonima, resultado:', r);
})