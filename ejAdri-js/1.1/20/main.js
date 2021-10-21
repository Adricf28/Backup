// Desarrolla un algoritmo que permita leer un valor entero positivo N y determinar si es primo o no

let num = 0

const isPrime = num => {
    for(let i = 2; i < num; i++)
      if(num % i === 0) return false;
    return num > 1;
  }

console.log(isPrime(2));  