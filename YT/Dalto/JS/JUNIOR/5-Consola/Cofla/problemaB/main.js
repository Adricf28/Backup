let estudiar = "100 minutos de estudio"
let practicas = "100 minutos de hacer trabajos practicos" 
let trabajar = "240 minutos de trabajo" 
let casa = "30 minutos de hacer cosas de la casa"
let descanso = "10 minutos de descanso"

console.log("TAREAS")

for (i = 0; i < 14; i++) {
    if (i == 0) {
        console.groupCollapsed('Semana 1')
    }
    console.groupCollapsed('Dia' + (i+1))
    console.log(trabajar);
    console.log(descanso);
    console.log(estudiar);
    console.log(practicas);
    console.log(casa);
    console.groupEnd();
    if (i == 7) {
        console.groupEnd();
        console.groupCollapsed('Semana 2');
    }
}

console.groupEnd();
console.groupEnd();