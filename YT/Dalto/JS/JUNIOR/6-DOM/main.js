// Jerarquia en el DOM:
// - Document es el nodo raiz, el cual contiene todos los demas nodos
// - Element son nodos definidos por etiquetas html
// - Text es el texto adentro de los nodos element
// - Attribute son los atributos de los element (en js se veran como info asociada a los element)
// - Comentarios, !DOCTYPE, etc tambien son nodos
// Mas y mejor info en https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeType


// let parrafo = document.getElementById("parrafo")
// let parrafo = document.getElementsByTagName("p")
// let parrafo = document.querySelector(".parrafo")
// let parrafo = document.querySelector("#parrafo")
// let parrafo = document.querySelectorAll(".parrafo")

// -------------------------------------------------------------------------------------------

// const rango = document.querySelector(".rango")

// rango.setAttribute("type","color")
// let valorDelAtributo = rango.getAttribute("type")
// rango.removeAttribute("type")

// document.write(valorDelAtributo)

// -------------------------------------------------------------------------------------------

// const titulo = document.querySelector(".titulo")

// titulo.setAttribute("contentEditable","false")
// titulo.setAttribute("dir","rtl")
// titulo.setAttribute("hidden","true")
// titulo.setAttribute("tabindex","0")
// titulo.setAttribute("title","anvorgueza depoio")

// -------------------------------------------------------------------------------------------

// const input = document.querySelector(".input-normal")

// input.className
// input.value
// input.type = "file"
// input.accept = "image/png"
// input.minLength = "4"
// input.placeholder = "tengomuchosueñojoder"
// input.required = " "

// -------------------------------------------------------------------------------------------

// const titulo = document.querySelector(".titulo")

// titulo.style.color = "#fff"
// titulo.style.backgroundColor = "#999"
// titulo.style.padding = "30px"
// titulo.style.display = "inline-block"

// titulo.classList.add("grande")
// titulo.classList.remove("grande")
// titulo.classList.toggle("grande")
// titulo.classList.replace("grande","chico")
// let valor = titulo.classList.item(1)
// let valor = titulo.classList.contains("blanco")
// console.log(valor);

// -------------------------------------------------------------------------------------------

// const titulo = document.querySelector(".titulo")

// let resultado = titulo.textContent
// let resultado = titulo.innerHTML
// console.log(resultado)

// -------------------------------------------------------------------------------------------

// const contenedor = document.querySelector(".contenedor")
// const fragmento = document.createDocumentFragment()

// for (i=0;i<20;i++){
//     const item = document.createElement("LI")
//     item.textContent = "Este es un item de la lista"
//     fragmento.appendChild(item)
// }
// contenedor.appendChild(fragmento)
// console.log(fragmento)

// -------------------------------------------------------------------------------------------

// const contenedor = document.querySelector(".contenedor")

// const primerHijo = contenedor.firstElementChild
// const ultimoHijo = contenedor.lastElementChild

// const hijos = contenedor.childNodes
// hijos.forEach(i => {
//     console.log(i);
// });

// const hijos2 = contenedor.children
// for (i of hijos2) {
//     console.log(i);
// }

// const h2Nuevo = document.createElement("H2")
// h2Nuevo.textContent = "Titulo"
// const h2Antiguo = document.querySelector(".h2")

// contenedor.replaceChild(h2Nuevo,h2Antiguo)
// contenedor.removeChild(h2Antiguo)
// let respuesta = h2Antiguo.hasChildNodes()
// let padre = h2Antiguo.parentElement
// console.log(h2Antiguo.previousElementSibling)
// console.log(h2Antiguo.nextElementSibling)

// -------------------------------------------------------------------------------------------

// const div3 = document.querySelector(".div3")

// console.log(div3.closest(".div"))