// window.onload espera a que todo el html cargue antes de ejecutar el script
// por si queremos colocar el <script> antes de <body>
window.onload = () => {
    const parrafo = document.getElementById('text')
    //innerText accede y modifica al texto del id que hayamos especificado
    //innerHTML puede añadir codigo html tambien
    // parrafo.innerText = 'Texto actualizado'
    parrafo.innerHTML = '<li>elemento1</li><li>elemento2</li>'
}

