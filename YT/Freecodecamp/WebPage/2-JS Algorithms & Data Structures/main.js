// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// ----------------------------------BASIC JAVASCRIPT------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------

// function multiplyAll(arr) {
//     var product = 1;
//     // Only change code below this line
//     for (var i = 0; i < arr.length; i++){
//       for (var j = 0; j < arr[i].length; j++){
//         product *= arr[i][j]
//     }
// }
//     // Only change code above this line
//     return product;
// }

// const multiplyAll = arr => {
//     var product = 1;
//     for (i in arr){
//         for (j in arr[i]){
//             product *= arr[i][j]
//         }
//     }
//     return product
// }
  
// console.log(multiplyAll([[1],[2],[3]]));
// console.log(multiplyAll([[1,2],[3,4],[5,6,7]]));
// console.log(multiplyAll([[5,1],[0.2, 4, 0.5],[3, 9]]));

// -----------------------------------------------------------------------------------

// // Setup
// var myArray = [];
// var i = 10;

// // Only change code below this line
// do {
//   myArray.push(i);
//   i++;
// }
// while (i < 10)

// console.log(myArray);
// console.log(i);

// ---------------------------------------------------------------------------------------

// function sum(arr, n) {
//     // Only change code below this line
//     if (n <= 0) {
//         return 0;
//     } else {
//         return sum(arr, n - 1) + arr[n - 1];
//     }
//     // Only change code above this line
// }

// console.log(sum([1], 0));
// console.log(sum([2, 3, 4], 1));
// console.log(sum([2, 3, 4, 5], 3));

// --------------------------------------------------------------------------------------

// // Setup

// // The function should check if name is an actual contact's firstName and the given property (prop) is a property of that contact.
// // If both are true, then return the "value" of that property.
// // If name does not correspond to any contacts then return the string No such contact.
// // If prop does not correspond to any valid properties of a contact found to match name then return the string No such property.

// var contacts = [
//     {
//         "firstName": "Akira",
//         "lastName": "Laine",
//         "number": "0543236543",
//         "likes": ["Pizza", "Coding", "Brownie Points"]
//     },
//     {
//         "firstName": "Harry",
//         "lastName": "Potter",
//         "number": "0994372684",
//         "likes": ["Hogwarts", "Magic", "Hagrid"]
//     },
//     {
//         "firstName": "Sherlock",
//         "lastName": "Holmes",
//         "number": "0487345643",
//         "likes": ["Intriguing Cases", "Violin"]
//     },
//     {
//         "firstName": "Kristian",
//         "lastName": "Vos",
//         "number": "unknown",
//         "likes": ["JavaScript", "Gaming", "Foxes"]
//     }
// ];


// function lookUpProfile(name, prop) {
//   // Only change code below this line
//     for (i in contacts) {
//         if (contacts[i]["firstName"] === name){
//             if (contacts[i].hasOwnProperty(prop)){
//                 return contacts[i][prop]
//             }else {
//                 return "No such property."
//             }
//         }
//     }
//     return "No such contact."
//   // Only change code above this line
// }

// console.log(lookUpProfile("Kristian", "lastName")); // should return the string Vos
// console.log(lookUpProfile("Sherlock", "likes")); // should return ["Intriguing Cases", "Violin"]
// console.log(lookUpProfile("Harry", "likes")); // should return an array
// console.log(lookUpProfile("Bob", "number")); // should return the string No such contact
// console.log(lookUpProfile("Bob", "potato")); // should return the string No such contact
// console.log(lookUpProfile("Akira", "address")) // should return the string No such property

// -------------------------------------------------------------------------------------

// // RANDOM NUMBER WITHIN A RANGE
// function randomRange(myMin, myMax) {
//     // Only change code below this line
//     return Math.floor(Math.random() * (myMax - myMin + 1)) + myMin
//     // Only change code above this line
// }

// ---------------------------------------------------------------------------------------

// const checkValue = (num) => {
//     return num > 0 ? "positive"
//          : num == 0 ? "zero"
//          : "negative"
// }

// console.log(checkValue(23));
// console.log(checkValue(0));
// console.log(checkValue(-23));

// ----------------------------------------------------------------------------------------

// function countup(n) {
//   console.log(n);
//   if (n < 1) {
//     return [];
//   } else {
//     const countArray = countup(n - 1);
//     countArray.push(n);
//     return countArray;
//   }
// }

// console.log(countup(1));

// --------------------------------------------------------------------------------------

// const countDown = (num) => {
//     if (num < 1) {
//         return []
//     } else {
//         const countArray = countDown(num - 1)
//         countArray.unshift(num)
//         return countArray
//     }
// }

// console.log(countDown(10));

// OTRA MANERA DE HACERLO

// function countdown(n){
//     return n < 1 ? [] : [n].concat(countdown(n - 1));
// }

// console.log(countdown(10));

// ---------------------------------------------------------------------------------------

// const rangeOfNumbers = (startNum, endNum) => {
//     return startNum > endNum 
//         ? [] 
//         : [startNum].concat(rangeOfNumbers(startNum+1,endNum))
// }

// console.log(rangeOfNumbers(4,4));

// OTRA MANERA DE HACERLO

// function rangeOfNumbers(startNum, endNum) {
//     if (endNum - startNum === 0) {
//       return [startNum];
//     } else {
//       var numbers = rangeOfNumbers(startNum, endNum - 1);
//       numbers.push(endNum);
//       return numbers;
//     }
// }

// console.log(rangeOfNumbers(1,4));

// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// ---------------------------------------ES6--------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------

// const MY_OBJECT = {
//     8 : "Levantarse",
//     9: "Estudiar"
// }

// Object.freeze(MY_OBJECT)

// MY_OBJECT[10] = "Seguir estudiando"

// console.log(MY_OBJECT);

// -----------------------------------------------------------------------------------

// const arrSum = (...args) => {
//     const sum = (preVal,currVal) => { return preVal + currVal }
//     return args.reduce(sum)
// }

// console.log(arrSum(1,2,3,4,5,6,7,8,9,10));

// -----------------------------------------------------------------------------------

// const myObj = {
//     hoy : "lentejas",
//     mañana : "macarrones"
// }

// const {hoy : today, mañana : tomorrow} = myObj

// console.log(today, tomorrow)

// ----------------------------------------------------------------------------------

// const myObj = {
//     estaSemana : {
//         hoy : "lentejas",
//         maniana : "macarrones"
//     }
// }

// const {estaSemana : thisWeek, estaSemana : {hoy : today, maniana : tomorrow}} = myObj

// console.log(thisWeek, today, tomorrow)

// -----------------------------------------------------------------------------------

// let myArray = [1,2,3,4,5,6,7,8,9,10]
// const [a,b,,,c, ...arr] = myArray
// console.log(a,b,c,arr);

// ------------------------------------------------------------------------------------

// const myObj = {
//     pesoMin : 63,
//     edad : 21,
//     estatura : 173,
//     pesoMax : 108,
//     ciudad : "Malaga"
// }

// const ranFun = ({pesoMin : min, pesoMax : max}) => (min + max) / 2

// console.log(ranFun(myObj))

// -----------------------------------------------------------------------------------

// const result = {
//     success: ["max-length", "no-amd", "prefer-arrow-functions"],
//     failure: ["no-var", "var-on-top", "linebreak"],
//     skipped: ["no-extra-semi", "no-dup-keys"]
// }

// function makeList(arr) {
//     // Only change code below this line
//     const failureItems = []
    
//     for (i in arr) {
//         failureItems.push(`<li class="text-warning">${arr[i]}</li>`)
//     }
//     // Only change code above this line
  
//     return failureItems;
// }
  
// const failuresList = makeList(result.failure);
// console.log(failuresList)

// ----------------------------------------------------------------------------------------

// const makeServerRequest = new Promise((resolve, reject) => {
//     // responseFromServer is set to true to represent a successful response from a server
//     let responseFromServer = false;
      
//     if(responseFromServer) {
//       resolve("We got the data");
//     } else {  
//       reject("Data not received");
//     }
// })
  
// makeServerRequest.then(result => {
//     console.log(result)
// })

// makeServerRequest.catch(error => {
//     console.log(error);
// })

// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// -------------------------------REGULAR EXPRESSIONS------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------

// let string = "Holaa buenaaas tardes 347816 bueno pos aqui estamos escribiendo cosas sin sentido alguno solo porque necesito una frase muuuuuuuuuuuuuuuuuy larga bueno hasta luego"
// let regex1 = /hola|una|porque|sentido/i
// let regex2 = /.en./gi
// let regex3 = /[a-z1-6]/gi
// let regex4 = /[^aeiou0-9]/gi
// let regex5 = /a+/gi //La a tiene que estar si o si una vez al menos
// let regex6 = /mu*/ig //La m seguido de 0 o mas u
// let regex7 = /^Hola/ //Match al principio de strings
// let regex8 = /luego$/ //Match al final de strings
// let regex9 = /\w/g //Equivale a [A-Za-z0-9_]
// let regex10 = /\W/g //Equivale a [^A-Za-z0-9_] hace match a espacios tambien
// let regex11 = /\d/g //Equivale a [0-9]
// let regex12 = /\D/g //Equivale a [^0-9]
// let regex13 = /\s/g //Match a espacios, tabs, etc
// let regex14 = /\S/g //Cualquier caracter que no sean espacios, tabs, etc
// let regex15 = /mu{4,6}.*/ //Match una m seguida de al menos 4 u y lo que sea despues
// let regex16 = /mu{4,}.../ //Match m seguida de al menos 4 u
// let regex17 = /buena{3}s/ //Match buenas con exactamente 3 a y una s despues
// let regex18 = /Holaa?/ //Question mark para que la letra anterior sea opcional
// let regex19 = /(Holaa|Buenaas).*(luego|pronto)/ //Hola|buenas seguido de cualquier cosa y acaba en luego|pronto
// let regex20 = /(\w+)(\s)\1\2\1/ // \1==primer parentesis, \2==segundo parentesis
// console.log(regex19.test(string))
// console.log(string.match(regex19))

// let string = "pin pan pun pon"
// let regex = /p[iau]n/ig
// console.log(string.match(regex))

// let string = "<h1>Buenas tarde</h1>"
// let regex = /<..*?>/i
// console.log(string.match(regex))

// ------------------------------------------------------------------------------------

// COMPROBANTE DE CONTRASEÑAS

//Primer caracter una letra, seguido de al menos otra letra y al final tiene 0 o mas digitos
//  O
//Primer caracter letra seguido de un digito y al menos otro digito mas al final
// let user = "Soniikz7"
// let userCheck = /^[a-z][a-z]+\d*$|^[a-z]\d\d+$/i
// console.log(userCheck.test(user))

//Greater than 5 character long and has 2 consecutive numbers
// let sampleWord = "12345";
// let pwRegex = /(?=\w{6,})(?=\w*\d{2})/; // Change this line
// let result = pwRegex.test(sampleWord);
// console.log(result)

// -------------------------------------------------------------------------------------

// REEMPLAZAR SI HACE MATCH Y INTERCAMBIAR ORDEN

// let string = "uno dos tres"
// let regex = /(\w+)\s(\w+)\s(\w+)/
// let newString = "$3 $1 $2"
// let resultado = string.replace(regex,newString)
// console.log(resultado)

// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// ------------------------------------DEBUGGING-----------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------

// function zeroArray(m, n) {
//     let newArray = [];
//     let row = [];
    
//     // Mete n cantidad de 0's en row
//     for (let j = 0; j < n; j++) {
//         row.push(0);
//     }

//     // Mete m cantidad de rows en newArray
//     for (let i = 0; i < m; i++) {
//       newArray.push(row);
//     }

//     return newArray;
// }
  
// let matrix = zeroArray(3, 2);
// console.log(matrix);

// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// -------------------------------BASIC DATA STRUCTURES----------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------

// function quickCheck(arr, elem) {
//     // Only change code below this line
//     return arr.indexOf(elem) == -1 ? false : true
//     // Only change code above this line
// }
  
// console.log(quickCheck(['squash', 'onions', 'shallots'], 'mushrooms'));

// ----------------------------------------------------------------------------------------

// function filteredArray(arr, elem) {
//     let newArr = [];
//     // Only change code below this line
//     for (i in arr) {
//         if (arr[i].indexOf(elem) == -1) {
//             newArr.push(arr[i])
//         }
//     }
//     // Only change code above this line
//     return newArr;
// }
  
// let array1 = [[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]]
// let elem1 = 13
// console.log(filteredArray(array1, elem1));

// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// -----------------------------BASIC ALGORITHM SCRIPTING--------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------

// function reverseString(str) {
//     return str.split("").reverse().join("")
// }
  
// console.log(reverseString("Greetings from Earth"))

// ------------------------------------------------------------------------------------------

// function factorialize(num) {
//     let factorial = 1
//     for (i = 1; i <= num; i++){
//         factorial *= i
//     }
//     return factorial
// }
  
// console.log(factorialize(0))

// -----------------------------------------------------------------------------------------

// LONGEST WORD OF STRING

// const longestWord = (str) => {
//     let regex = /\s/ // SOBRA
//     let array1 = str.split(regex) // ES MEJOR PONER " " AQUI Y YA ESTA
//     let longestWord = ""
//     for (i of array1) {
//         if (i.length > longestWord.length) {
//             longestWord = i
//         }
//     }
//     return longestWord
// }

// console.log(longestWord("The quick brown fox jumped over the lazy dog"))

// ----------------------------------------------------------------------------------------

// CREAR ARRAY CON LOS NUMEROS MAS GRANDES DE OTROS 4 SUB-ARRAYS

// const largestOfFour = (arr) => {
//     let newArr = []
//     let largerNum
//     for (i in arr) {
//         for (j in arr[i]) {
//             if (j == 0) {
//                 largerNum = arr[i][j]
//             }
//             if (arr[i][j] > largerNum){
//                 largerNum = arr[i][j]
//             }
//         }
//         newArr.push(largerNum)
//         largerNum = undefined
//     }
//     return newArr
// }

// let ejArr = [[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]
// let ejArr2 = [[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]
// let ejArr3 = [[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]
// console.log(largestOfFour(ejArr))
// console.log(largestOfFour(ejArr2))
// console.log(largestOfFour(ejArr3))

// ----------------------------------------------------------------------------------------

// COMPROBAR SI UN STRING TERMINA CON TARGET, CON .endsWith() ES INFINITAMENTE MAS FACIL

// const confirmEnding = (str, target) => {
//     return str.slice(str.length - target.length) === target;
// }
  
// console.log(confirmEnding("Bastian", "n"))

// ---------------------------------------------------------------------------------------

// REPETIR UN STRING(STR) UN NUMERO(NUM) DE VECES

// const repeatStringNumTimes = (str, num) => {
//     let string = ""
//     if (num > 0) {
//         for (i = 0; i < num; i++) {
//             string += str
//         }
//     } else {
//         return ""
//     }
//     return string
// }
  
// console.log(repeatStringNumTimes("abc", 2))

// ----------------------------

// MANERA MAS OPTIMA DE HACERLO

// function repeatStringNumTimes(str, num) {
//     return num > 0 ? str + repeatStringNumTimes(str, num - 1) : '';
// }

// ---------------------------------------------------------------------------------------

// CORTAR UN STRING(STR) SI SE PASA DE LA LONGITUD MAXIMA ESPECIFICADA(NUM)

// const truncateString = (str, num) => {
//     return str.length > num ? str.slice(0, num) + "..." : str
// }
// console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8))

// ----------------------------------------------------------------------------------------

// ENCONTRAR EL PRIMER PAR DE UN ARRAY

// const findElement = (arr, func) => {
//     for (i of arr) {
//         if (func(i) === true) {
//             return i
//         }
//     }
//     return undefined
// }
  
// console.log(findElement([45, 1, 3, 4], num => num % 2 === 0))

// ---------------------------

// MANERA MAS OPTIMA DE HACERLO

// const findElement = (arr, func) => {
//     return arr.find(func)
// }
// The find() method returns the value of the first element in the provided array that satisfies the provided testing function. If no values satisfy the testing function, undefined is returned.

// ---------------------------------------------------------------------------------------

// UPPERCASE EACH LETTER OF EACH WORD OF A STRING
// const titleCase = (str) => {
//     return str.toLowerCase().split(" ").map(val => val.replace(val.charAt(0),val.charAt(0).toUpperCase())).join(" ");
// };
  
// console.log(titleCase("HERE IS MY HANDLE HERE IS MY SPOUT"));

// --------------------------------------------------------------------------------------

// ADD ORDERED ARRAY AT N INDEX OF ANOTHER ARRAY

// MY TRY

// const frankenSplice = (arr1, arr2, n) => {
//     let arr3 = arr2.slice(0,n);
//     arr1.forEach(i => {
//         arr3.push(i);
//     });
//     arr2.forEach(i => {
//        if (!(arr3.includes(i))) {arr3.push(i)};
//     });
//     return arr3;
// };

// -----------------------

// BEST WAY TO DO IT, USING ... TO ADD EACH ITEM OF ARRAY

// const frankenSplice = (arr1, arr2, n) => {
//     let arr3 = arr2.slice(); // COPIA EXACTA DE ARR2, USANDO SLICE PERO SIN CORTAR NADA
//     arr3.splice(n,0,...arr1);
//     return arr3;
// };
  
// console.log(frankenSplice([1, 2, 3], [4, 5], 1));
// console.log(frankenSplice([1, 2], ["a", "b"], 1));
// console.log(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2));
// console.log(frankenSplice([1, 2, 3, 4], [], 0));

// ------------------------------------------------------------------------------------------

// BORRAR VALORES FALSY DE ARRAY

// MI INTENTO (DESPUES DE PROBAR MIL COSAS Y DE AQUELLA MANERA, SIN SABER NADA DE TRUTHY Y FALSY)

// const bouncer = (arr) => {
//    const falsy = [false, null, 0, "", undefined, NaN];
//    for (i in falsy) {
//        for (k in arr) {
//         if (arr[k] == falsy[i]) {
//             arr.splice(k,1);
//             if (isNaN(arr[k])) {
//                 arr.splice(k,1);
//             }
//         }
//        }
//    }
//    return arr;
// };

// ---------------------

// CON LA PISTA DE USAR .filter()

// const falsy = (word) => {
//     const falsyArr = [false, null, 0, "", undefined, NaN];
//     return falsyArr.includes(word) ? false : true;
// };

// const bouncer = (arr) => {
//     let filtered = arr.filter(falsy);
//     return filtered;
// };

// ---------------------

// SABIENDO QUE IF(X) SIEMPRE ES TRUE A NO SER QUE X SEA UN VALOR FALSY (false, null, 0, "", undefined, NaN), ESTA ES LA MANERA MAS OPTIMA

// const bouncer = (arr) => {
//     let filtered = [];
//     for (i of arr) {
//         if (i) filtered.push(i);
//     }
//     return filtered;
// };


// console.log(bouncer([7, "ate", "", false, 9]));
// console.log(bouncer(["a", "b", "c"]));
// console.log(bouncer([false, null, 0, NaN, undefined, ""]));
// console.log(bouncer([null, NaN, 1, 2, undefined]));

// ----------------------------------------------------------------------------------------

// MY TRY

// const getIndexToIns = (arr,num) => {
//     const orderedArr = arr.sort((a, b) => a - b);
//     let index;
//     if (orderedArr.length != 0) {
//         for (i in orderedArr) {
//             if (orderedArr[i] >= num) {
//                 return parseInt(index = i);
//             } else if (orderedArr[i] < num) {
//                 index = orderedArr.length;
//             }
//         }
//     } else {
//         index = 0;
//     }
//     return index;
// };

// ---------------------

// DOS MANERAS MEJORES DE HACERLO

// MI CODIGO PERO OPTIMIZADO
// function getIndexToIns(arr, num) {
//     arr.sort((a, b) => a - b);
//     for (let i = 0; i < arr.length; i++) {
//       if (arr[i] >= num) {
//           return i;
//       }
//     }
//     return arr.length;
// };

// MAS INTELIGENTE
// const getIndexToIns = (arr, num) => {
//     return arr
//       .concat(num) // METO EL NUMERO EN EL ARRAY
//       .sort((a, b) => a - b) // ORDENO EL ARRAY
//       .indexOf(num); // Y EL NUMERO SE QUEDA EN LA POSICION QUE QUIERO
// };

// console.log(getIndexToIns([10, 20, 30, 40, 50], 35)); // 3
// console.log(getIndexToIns([10, 20, 30, 40, 50], 30)); // 2
// console.log(getIndexToIns([40, 60], 50));  // 1
// console.log(getIndexToIns([3, 10, 5], 3)); // 0
// console.log(getIndexToIns([5, 3, 20, 3], 5)); // 2
// console.log(getIndexToIns([2, 20, 10], 19)); // 2
// console.log(getIndexToIns([2, 5, 10], 15)); // 3
// console.log(getIndexToIns([], 1)); // 0

// ------------------------------------------------------------------------------------------

// const mutation = (arr) => {
//     let word1 = arr[0].toLowerCase().split("");
//     let word2 = arr[1].toLowerCase().split("");
//     for (i in word2) {
//         if (word1.indexOf(word2[i]) == -1) {
//             return false;
//         }
//     }
//     return true;
// };

// console.log(mutation(["hello", "hey"])); // false
// console.log(mutation(["hello", "Hello"])); // true
// console.log(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"])); // true
// console.log(mutation(["Mary", "Army"])); // true
// console.log(mutation(["Mary", "Aarmy"])); // true
// console.log(mutation(["Alien", "line"])); // true 
// console.log(mutation(["floor", "for"])); // true
// console.log(mutation(["hello", "neo"])); // false
// console.log(mutation(["voodoo", "no"])); // false
// console.log(mutation(["ate", "date"])); // false
// console.log(mutation(["Tiger", "Zebra"])); // false
// console.log(mutation(["Noel", "Ole"])); // true

// --------------------------------------------------------------------------------------

// DIVIDIR UN ARRAY EN OTRO ARRAY CON SUB-ARRAYS DE "SIZE" LONGITUD

// MI INTENTO (REGULAR PERO FUNCIONAL)

// const chunkArrayInGroups = (arr, size) => {
//     let bigArr = [];
//     let lilArr = [];
//     let index = 0;
//     for (i in arr) {
//         if (index < size) {
//             lilArr.push(arr[i]);
//             index++; 
//         } else {
//             bigArr.push(lilArr);
//             lilArr = [];
//             index = 0;
//             lilArr.push(arr[i]);
//             index++;
//         }
//     }
//     bigArr.push(lilArr);
//     return bigArr;
// };

// -----------------------

// MEJOR MANERA

// const chunkArrayInGroups = (arr, size) => {
//     let newArr = [];
//     while (arr.length > 0) {
//       newArr.push(arr.splice(0, size));
//     }
//     return newArr;
// };

// console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2), "2");
// console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3), "3");
// console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2), "2");
// console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4), "4");
// console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3), "3");
// console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4), "4");
// console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2), "2");

// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// ----------------------------OBJECT ORIENTED PROGRAMMING-------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------

// Manera de crear funciones y llamarlas instantaneamente
// (function(){console.log("Buenos dias");})();

// -------------------------------------------------------------------------------------

// Own properties: diferentes para cada instancia
// function Dog(name,color) {
//     this.name = name;
//     this.color = color;
// };

// const tina = new Dog("Tina","Canela");

// // instanceof verifica si una variable es una instancia de un constructor
// // console.log(tina instanceof Dog);

// // Comprobar si tina hereda el prototype de Dog
// // console.log(Dog.prototype.isPrototypeOf(tina));

// // Prototype properties: Propiedad para todas las instancias de Dog, la manera mas optima
// // Dog.prototype.numLegs = 4;

// // La mejor manera de definir prototype properties: 
// Dog.prototype = {
//     constructor: Dog, // Deberia definirse siempre la propiedad constructor
//     numLegs: 4,
//     tails: 1,
//     describe: () => {console.log(`My name is ${this.name}`);},
//     eat: function() {
//         console.log("nom nom nom");
//     },
//     ears: 2
// }

// // Identificar own properties y prototype properties
// let ownProperties = [];
// let prototypeProperties = [];

// for (let property in tina) {
//     if (tina.hasOwnProperty(property)) {
//         ownProperties.push(property);
//     } else {
//         prototypeProperties.push(property);
//     }
// }

// -----------------------------------------------------------------------------------------

// INHERITANCE

// function Person(name,age){
//     this.name = name;
//     this.age = age;
// };

// Person.prototype = {
//     constructor : Person,
//     ears : 2,
//     legs : 2,
//     saludar : function() {
//         console.log(`Hello my name is ${this.name} and i'm ${this.age} years old. Obviously i have ${this.ears} ears and ${this.legs} legs like most people.`);
//     }
// };

// let adrian = new Person("Adrian",21);
// // adrian.saludar();

// function Ninio(name, age){
//     this.name = name;
//     this.age = age;
// };

// // Asi el prototype de ninio hereda todo lo del prototype Person
// Ninio.prototype = Object.create(Person.prototype);
// Ninio.prototype.constructor = Ninio;

// Ninio.prototype.darPorCulo = function(){
//     console.log("waaaaaa waaaaaaaaa noseque soy un niño mira como lloro dame de comer jajaj pataaaaaaaaaaaaaaaaaaaaaaaata.");
// };

// // Puedes sobreescribir metodos heredados para las instancias
// Ninio.prototype.saludar = function(){
//     console.log("Anjo anjo asdf eof hdsnasop soy un puto retrasado fdshfsiodfha");
// };

// let paquillo = new Ninio("Paquillo", 5);

// paquillo.saludar();
// paquillo.darPorCulo();

// -------------------------------------------------------------------------------------------

// Variable privada y getter

// function Bird(){
//     let weight = 15;
//     this.getWeight = function(){return weight;};
// };

// -----------------------------------------------------------------------------------------

// function person(name){this.name = name;};
// function parrot(name){this.name = name;};

// let oze = new person("Oze");
// let wanillo = new parrot("Wanillo");

// // IIFE que devuelve un objeto con dos keys cuyos values son funciones a las que les pasas un objeto y le asigna un par key-value
// let funModule = (function () {
//     return {
//       isCuteMixin: function(obj) {
//         obj.isCute = function() {
//           return true;
//         }
//       },
//       singMixin: function(obj) {
//         obj.sing = function() {
//           console.log("Brrrr las colta los palo noeque noecuanto te meto tres tiro pum pum pum");
//         }
//       }
//     }
// }) ();

// funModule.singMixin(oze);
// funModule.singMixin(wanillo);

// oze.sing();
// wanillo.sing();