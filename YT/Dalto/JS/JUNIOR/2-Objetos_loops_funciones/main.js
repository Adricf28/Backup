// let pc1 = {
//     nombre : 'AdrianPC',
//     cpu : 'Ryzen 7',
//     ram : '16GB',
//     ssd : '1TB'
// }

// let pc2 = ['AdrianPC', 'Ryzen 7', '16GB', '1TB']

// let nombre = pc1['nombre']
// let cpu = pc1['cpu']
// let ram = pc1['ram']
// let ssd = pc1['ssd']

// let frase = `Mi PC se llama ${nombre}, <br>
//             el procesador es el ${cpu}, <br>
//             tiene ${ram} de ram, <br>
//             y ${ssd} de ssd.`

// document.write(frase)



// let num1 = 0

// while (num1 < 20) {
//     num1++
//     console.log(`El número es ${num1}. `);
//     if (num1 === 10) {
//         continue
//     }
//     if (num1 === 11) {
//         console.log('Felisidade bro');
//         break
//     }
// }



// for (let i = 0; i < 6; i++) {
//     console.log(`Numero ${i}`); 
// }



// let animales = {
//     an1 : 'perro',
//     an2 : 'gato',
//     an3 : 'hamster'
// }

// for (i in animales) {
//     console.log(`${i}: ${animales[i]}`);
// }
// for (i of animales) {
//     console.log(animales[i]);
// }



// let array1 = ['paco', 'pepe', 'jose']
// let array2 = ['manue', 'luis', array1]

// for (i in array2) {
//     if (i == 2) {
//         for (i of array1) {
//             console.log(i);
//             continue
//         }
//     }
//     else {
//         console.log(array2[i]);
//     }
// }



// function greetings(n){
//     let respuesta = prompt(`How are you ${n}?`) 
//     if (respuesta == 'good') {
//         alert('Nice')
//     } else {
//         alert('Why man?')
//     }
// }

// greetings('adrian')



const saludar = nombre => console.log(`Buenas tardes, ${nombre}.`);

saludar('Adrián')
