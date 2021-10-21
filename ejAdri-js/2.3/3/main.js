// Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno se entiende que están comprendidas entre 0 y 10. Guardarlas en una lista y ordenarlas de mayor a menor.

let notas = []

for (i = 0; i < 5; i++) {
    let nota = parseFloat(prompt("Introduce tus notas"))
    if (nota < 0 || nota > 10) {
        document.write("Las notas deben ser entre 0 y 10");
        break
    } else {
        notas.push(nota)
    }
}

notas.length === 5 ? notas.sort() && document.write(notas) : ""