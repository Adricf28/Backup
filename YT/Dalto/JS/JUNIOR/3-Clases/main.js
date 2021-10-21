class Animal {
    constructor(especie,edad,color){
        this.especie = especie
        this.edad = edad
        this.color = color
        this.info = `Soy un ${this.especie}, tengo ${this.edad} años y soy de color ${this.color}.`
    }
    verInfo() {
        document.write(this.info + "<br>")
    }
}

class Perro extends Animal {
    constructor(especie, edad, color, raza) {
        super(especie, edad, color)
        this.raza = null
    }
    static ladrar(perro){
        console.log("guau");
    }
    set setRaza(raza){
        this.raza = raza
    }
    get getRaza(){
        return this.raza
    }
}


const pastorAleman = new Perro('perro',5,'marron',"pastor aleman")
const gato = new Animal('gato',8,'negro')
const periquito = new Animal('periquito',1,'verde')

pastorAleman.setRaza = "doberman"
console.log(pastorAleman.getRaza);
