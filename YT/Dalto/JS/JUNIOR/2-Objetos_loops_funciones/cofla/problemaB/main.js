// En un curso con x cantidad de alumnos se rompió el sistema de registro de asistencias durante 30 dias, y hay que crear un sistema que permita registrar alumnos presentes (P) y ausentes (A). Pasados los 30 dias mostrar la situación final de todos los alumnos (num total de presentes y ausentes). Se puede tener un máximo de 10% de ausencias por semestre, si se tienen más declarar que está suspenso . 

let cantidad = prompt('Cuantos alumnos son?')
let alumnosTotales = []

// Añadir alumnos al array de alumnosTotales
for (i = 0; i < cantidad; i++) {
    alumnosTotales[i] = [prompt(`Nombre del alumno ${i+1}:`),0]
}

// Aumentar el numero de presencias(segundo valor de cada array de alumno) si se da el caso
const pasarLista = (name,position) => {
    let presencia = prompt(`${name}, presente?`)
    if (presencia == 'p' || presencia == 'P') {
        alumnosTotales[position][1]++
    }
}

// Pasar lista 30 veces, consultando la asistencia de todos los alumnos cada vez
for (i = 0; i < 30; i++) {
    for (alumno in alumnosTotales) {
        pasarLista(alumnosTotales[alumno][0],alumno)
    }
}

// Muestra los resultados ya obtenidos despues de 30 dias
for (alumno in alumnosTotales) {
    let resultado = `<b>${alumnosTotales[alumno][0]}</b>:<br>
    _______Asistencias: ${alumnosTotales[alumno][1]} <br>
    _______Ausencias: ${30 - parseInt(alumnosTotales[alumno][1])}`
    if (30 - alumnosTotales[alumno][1] > 18) {
        resultado += '<b style="color: red;"> SUSPENSO POR NO ASISTIR</b><br><br>'
    }else {
        resultado += "<br><br>"
    }
    document.write(resultado)
}