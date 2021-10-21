// Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

let strList = []

for (i = 0; i < 3; i++) {
    let string = prompt("Write anything")
    strList.push(string)
}

document.write(`<b>Ordered array:</b> <br>
${strList[0]} <br>
${strList[1]} <br>
${strList[2]} <br> <br>`)

let copyList = []
strList.forEach(i => {
    copyList.push(i)
});
copyList.reverse()

document.write(`<b>Disordered array:</b> <br>
${copyList[0]} <br>
${copyList[1]} <br>
${copyList[2]} <br> <br>`)