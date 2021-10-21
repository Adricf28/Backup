console.log("%cPara aprobar este semestre, el alumno debera cumplir todos los siguientes requisitos: \n - Haber acudido a al menos el 90% de las 180 clases. \n - Haber entregado al menos el 75% de los 12 trabajos de este curso. \n - Tener al menos una nota media de 7 entre todas las materias.","color:#50a2e7;")

const aprobado = (name) => {
    
    let asistencias = parseFloat(prompt("Introduce tu numero de asistencias totales este semestre"))
    if (asistencias >= 162) {
        console.log("%c+1 punto por contar con al menos el 90% de las asistencias","color:#a5e994;")
    } else {
        return console.log(`%c${name} no cuenta con al menos el 90% de las asistencias, por lo tanto, ha suspendido este semestre.`,"color:red;")
    }


    let trabajos = parseFloat(prompt("Introduce cuantos de los 12 trabajos de este curso has realizado."))
    if (trabajos >= 9) {
        console.log("%c+1 punto por haber entregado al menos el 75% de los trabajos","color:#a5e994;")
    } else {
        return console.log(`%c${name} no cuenta con al menos el 75% de los trabajos entregados, por lo tanto, ha suspendido este semestre.` ,"color:red;")
    }


    let fisica = parseFloat(prompt("Introduce tu nota de fisica"))
    let programacion = parseFloat(prompt("Introduce tu nota de programacion"))
    let logica = parseFloat(prompt("Introduce tu nota de logica"))
    let quimica = parseFloat(prompt("Introduce tu nota de quimica"))
    let media = (fisica + programacion + logica + quimica) / 4
    
    if (media >= 7) {
        console.log("%c+1 punto por tener al menos una media de 7 en los examenes de todas las materias","color:#a5e994;")
    } else {
        return console.log(`%c${name} no cuenta con una media de al menos 7 en los examenes, por lo tanto, ha suspendido este semestre`,"color:red;")
    }

    return console.log(`%c${name} ha cumplido todos los requisitos para aprobar, felicidades.`,"color:#00ff41;")

}

aprobado(prompt("Nombre del alumno"))
aprobado(prompt("Nombre del alumno"))