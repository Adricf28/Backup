const todos = ['1','2','3','4','5','6']
let xd = []

let map = todos.map(t => '<li>' + t + '</li>')
console.log('TODOS:',todos);
console.log('MAP:',map);
xd = [map.join('SI')]
console.log(xd);

// var cadena = '{"nombre":"Adrian","edad":"21","pais":"españa"}'
// var objetoJS = JSON.parse(cadena)
// var stringJSON = JSON.stringify(objetoJS)

// console.log('Cadena:',typeof cadena,cadena);
// console.log('StringJSON:',typeof stringJSON, stringJSON);
// console.log('ObjetoJS:',typeof objetoJS, objetoJS);