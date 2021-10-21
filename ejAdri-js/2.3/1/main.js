// Crea una lista con 3 cadenas de caracteres leídas por teclado.

let strList = []

for (i = 0; i < 3; i++) {
    let string = prompt("Write anything")
    strList.push(string)
}

document.write(`${strList[0]} <br>
                ${strList[1]} <br>
                ${strList[2]}`)