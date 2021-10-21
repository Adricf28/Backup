// MI INTENTO
// class Movil {
//     constructor(color,peso,pantRes,camRes,ram){
//         this.color = color
//         this.peso = peso 
//         this.pantRes = pantRes
//         this.camRes = camRes
//         this.ram = ram
//     }
//     info(){
//         return `Este telefono es ${this.color}, pesa ${this.peso} gramos, tiene una resolucion ${this.pantRes} y una camara de ${this.camRes} megapíxeles, además de ${this.ram} gb de ram.`
//     }
//     encender(){
//         console.log("Introduce tu contraseña.");
//     }
//     reiniciar(){
//         console.log("Preparando para el reinicio...");
//     }
//     apagar(){
//         console.log("Buenas noches.");
//     }
//     fotografiar(){
//         console.log("Foton bro");
//     }
//     grabar(){
//         console.log("Mira como tira la cashimba surmano.");
//     }
// }

// const lg = new Movil("azul",140,"HD",10,2)
// const xiaomi = new Movil("negro",120,"full hd",11,3)
// const alcatel = new Movil("blanco",170,"HD",8,1)

// xiaomi.encender()
// xiaomi.fotografiar()
// xiaomi.grabar()




// VERSION DALTO
class Celular {
    constructor(color,peso,rdp,rdc,ram){
        this.color = color
        this.peso = peso
        this.resPant = rdp
        this.resCam = rdc
        this.ram = ram
        this.encendido = false
    }
    onOff(){
        if (this.encendido == false){
            alert("Celular prendido")
            this.encendido = true
        }else {
            alert("El celular se apago")
            this.encendido = false
        }
    }
    reiniciar(){
        if (this.encendido == true) {
            alert("Reiniciando celular")
        }else {
            alert("El celular esta apagado")
        }
    }
    tomarFotos(){
        alert(`Foto tomada en una resolucion de ${this.resCam}`)
    }
    grabar(){
        alert(`Grabando video en ${this.resCam}`)
    }
    verInfo(){
        return `
        Color: <b>${this.color}</b> <br>
        Peso: <b>${this.peso}</b> <br>
        Tamaño: <b>${this.resPant}</b> <br>
        Resolucion de cámara: <b>${this.resCam}</b> <br>
        RAM: <b>${this.ram}</b> <br>
        `
    }
}

const celular1 = new Celular("rojo","150g","5'","HD","1GB")
const celular2 = new Celular("negro","155g","5.4'","full HD","2GB")
const celular3 = new Celular("blanco","146g","5.9'","full HD","2GB")

document.write(`
    ${celular1.verInfo()} <br>
    ${celular2.verInfo()} <br>
    ${celular3.verInfo()}
`)