const info = materia => {
    let materias = {
        física : ["Perez","Pedro","Pepe","Cofla","Maria"],
        programacion : ["Dalto","Pedro","Juan","Pepe"],
        lógica : ["Hernandez","Pedro","Juan","Pepe","Cofla","Maria"],
        química : ["Rodriguez","Pedro","Juan","Pepe","Cofla","Maria"]
    }
    if (materias[materia] !== undefined) {
        return [materia,materias[materia]]
    } else {
        return materias
    }
}

const obtenerInfo = materia => {
    let informacion = info(materia)
    let materias = info()
    let clases = Object.keys(materias)
    if (clases.includes(materia)) {
        let clase = informacion[0]
        let profesor = informacion[1][0]
        let alumnos = informacion[1]
        alumnos.shift()
        console.log(`Alumnos presentes en la clase de ${clase} del señor ${profesor}: ${alumnos}`);
    } else {
        console.log("Esa materia no existe."); 
    }
}

const classNum = alumno => {
    let contador = 0
    let clases = []
    let materias = info()
    for (i in materias){
        if (materias[i].includes(alumno)){
            let profesor = materias[i][0]
            contador++
            clases.push(` ${i}(del profesor ${profesor})`)
        }
    }
    console.log(`${alumno} esta en ${contador} clases:${clases}.`);
}

obtenerInfo("química")
obtenerInfo("joseluis")
obtenerInfo()
classNum("Cofla")