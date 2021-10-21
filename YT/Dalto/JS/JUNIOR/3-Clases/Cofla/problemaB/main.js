class Teléfono {
    constructor(color,peso,tamaño,resCam,ram){
        this.color = color
        this.peso = peso
        this.tamaño = tamaño
        this.resCam = resCam
        this.ram = ram
        this.encendido = false
    }
    onOff(){
        if (this.encendido == false){
            alert("Teléfono encendido.")
            return this.encendido = true
        }else {
            alert("Teléfono apagado")
            return this.encendido = false
        }
    }
    reiniciar(){
        if (this.encendido == true) {
            alert("Reiniciando teléfono")
        }else {
            alert("El teléfono esta apagado")
        }
    }
    hacerFotos(){
        alert(`Foto tomada en una resolucion ${this.resCam}`)
    }
    grabar(){
        alert(`Grabando video en ${this.resCam}`)
    }
    verInfo(){
        return `
        Color: <b>${this.color}</b> <br>
        Peso: <b>${this.peso}</b> <br>
        Tamaño: <b>${this.tamaño}</b> <br>
        Resolucion de cámara: <b>${this.resCam}</b> <br>
        RAM: <b>${this.ram}</b> <br>
        `
    }
}

const lg = new Teléfono("rojo","150g","5'","HD","1GB")
const xiaomi = new Teléfono("azul","155g","5.4'","full HD","2GB")
const alcatel = new Teléfono("blanco","146g","5.9'","full HD","2GB")


class AltaGama extends Teléfono {
    constructor(color,peso,tamaño,resCam,ram,extraCamRes){
        super(color,peso,tamaño,resCam,ram)
        this.extraCamRes = extraCamRes
        this.cara = true
    }
    superSlowCam(){
        if (this.encendido == true){
            alert(`Videaso a 1000 fps con tu camara ${this.resCam} bro.`)
        } else {
            alert("Enciende el telefono antes de intentar grabar.")
        }
    }
    facialRec(){
        if (this.cara == true){
            alert("Teléfono desbloqueado por reconocimiento facial correctamente.")
        } else {
            alert("Coloque su cara frente a la camara del teléfono para poder reconocerla.")
        }
    }
    infoAltaGama(){
        return this.verInfo() + `Resolucion de camara extra: <b>${this.extraCamRes}</b>`
    }
}

const iphone = new AltaGama("gris","140g","6'","full HD","4GB","4k")
const samsung = new AltaGama("negro","145g","5.7'","full HD","4GB","2k")


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