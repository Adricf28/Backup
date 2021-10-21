class App {
    constructor(name,numDesc,rating,peso){
        this.name = name
        this.numDesc = numDesc
        this.rating = rating
        this.peso = peso
        this.espacio = 3
        this.instalada = false
        this.abierta = false
    }
    showInfo(){
        console.log(`${this.name} fue descargada por ${this.numDesc} de personas, las cuales le dieron una puntuacion de ${this.rating}/5 y pesa ${this.peso}GB`);
    }
    instalar(){
        if (this.peso <= this.espacio) {
            this.espacio -= parseFloat(this.peso)
            console.log(`App instalada correctamente, ha ocupado ${this.peso}GB. Te quedan ${this.espacio}GB disponibles.`);
            this.instalada = true
        } else {
            console.log(`No se ha podido instalar, la app pesa ${this.peso - this.espacio}GB más de los que tienes disponibles.`);
        }
    }
    abrirApp(){
        if (this.instalada == true) {
            console.log("Abriendo app...");
            this.abierta = true
        }
        else {
            console.log("Instale la app antes de intentar abrirla.");
        }
    }
    cerrarApp(){
        if (this.instalada == true && this.abierta == true) {
            console.log("Cerrando app...");
        } 
        else if(this.instalada == true && this.abierta == false){
            console.log("No puede cerrar la app si no esta abierta.");
        } else {
            console.log("Instale la app antes de intentar cerrarla.");
        }
    }
    desinstalarApp(){
        if (this.instalada == true) {
            console.log("Desinstalando app...");
        } else {
            console.log("No puede desinstalar una app que no tiene instalada.");
        }
    }
}

const geometryDash = new App("Geometry Dash","+5M","4.7","1.8")
const candyCrush = new App("Candy Crush","+1B","4.6","2")
const cookieClicker = new App("Cookie Clicker","1.2M","4.7","0.8")