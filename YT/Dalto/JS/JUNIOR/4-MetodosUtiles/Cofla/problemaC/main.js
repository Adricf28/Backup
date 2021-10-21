let materias = {
    física : ["Perez","Pedro","Pepe","Maria","Adrian","Amara","Yoni","Francisco","Monica","Rosa","Alejandro","Antonio"],
    programación : ["Dalto","Pedro","Pepe","Maria","Adrian","Amara","Yoni","Francisco","Monica","Rosa","Alejandro","Antonio","Jorge","Jose","Diego","Ismael","Paula"],
    lógica : ["Hernandez","Pedro","Pepe","Maria","Adrian","Amara","Yoni","Francisco","Monica","Rosa","Alejandro","Antonio","Jorge","Jose","Diego","Ismael","Paula","Raquel","Laura","Alberto","Manuel"],
    química : ["Rodriguez","Pedro","Pepe","Maria","Adrian","Amara","Yoni","Francisco","Monica","Rosa","Alejandro","Antonio","Jorge","Jose","Diego","Ismael","Paula","Raquel","Laura","Alberto","Pablo","Roberto","Felix"]
}


const inscripcion = clase => {
    let clases = []
    for (i in materias) {
        clases.push(i)
    }
    if (clases.includes(clase)) {
        if (materias[clase].length < 21) {
            materias[clase].push("Cofla")
            console.log(`Cofla se inscribio a la clase de ${clase}.`);
        } else {
            console.log(`La clase de ${clase} tiene ${materias[clase].length - 1} alumnos, asi que ya esta llena`);
        }
    } else {
        console.log(`La materia ${clase} no existe.`);
    }
}

inscripcion("física")
inscripcion("programación")
inscripcion("lógica")
inscripcion("química")