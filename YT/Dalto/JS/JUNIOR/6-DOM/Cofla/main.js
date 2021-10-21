const contenedor = document.querySelector(".flex-container")
const fragmento = document.createDocumentFragment()

const crearLlave = (nombre,modelo,precio) => {
    img = "<img src='llave.png' alt='llave.png'>"
    nombre = `<h2>${nombre}</h2>`
    modelo = `<h3>${modelo}</h3>`
    precio = `<h3 class='precio'>${precio}</h3>`
    return [img, nombre, modelo, precio]
}

for (i=0;i<20;i++){
    let randomModel = Math.round(Math.random()*10000)
    let randomPrice = (Math.random()*10+30).toFixed(2)
    let llave = crearLlave(`Llave ${i+1}`, `Modelo ${randomModel}`, `Precio: <b>${randomPrice}€</b>`)
    let div = document.createElement("div")
    div.addEventListener("click",()=>{document.querySelector(".key-data").value = randomModel})
    div.tabIndex = i
    div.classList.add(`flex-item`,`item${i}`)
    div.innerHTML += llave[0] + "<br>" + llave[1] + "<br>" + llave[2] + "<br>" + llave[3] + "<br><br>"
    fragmento.appendChild(div)
}
contenedor.appendChild(fragmento)