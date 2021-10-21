const datos = [{
    id: 1,
    title: 'Iron Man',
    year: 2008
},{
    id: 2,
    title: 'Spiderman: Homecoming',
    year: 2017
},{
    id: 3,
    title: 'Avengers: Endgame',
    year: 2019
}];

const datos2 = [{
    id: 1,
    title: 'Shutter Island',
    year: 2010
}]

const getDatos = () => {
    console.log('Esperando a los datos...');
    return new Promise((resolve,reject) => {
        if (datos2.length === 0) {
            reject(new Error('No existen datos'))
        }
        setTimeout(() => {
            resolve(datos2);
        }, 1500)
        
    }) 
}

// getDatos()
//     .then((datos)  => {
//         datos.push({
//             id: 2,
//             title: 'Creed 2',
//             year: 2018
//         })
//         console.log(datos);
//     })
//     .then(() => {
//         console.log('Armondiga')
//     })
//     .catch()

// async function fetchingData () {
//     try {
//         const datosFetched = await getDatos()
//         datos2.push({
//             id: 2,
//             title: 'Creed 2',
//             year: 2018
//         })
//         console.log(datosFetched);
//     } catch (err) {
//         console.log(err.message);
//     }
// }

// fetchingData()

Promise.resolve(2)
    .then(valor => Promise.reject(1))
    .then(valor => Promise.reject(valor))
    .catch(e => console.error('ERROR:',e))

new Promise((resolve,reject)=>{
    setTimeout(()=>reject(2),1000)
})
.then(x => console.log(x))
.catch(e=>console.error('Error:',e))