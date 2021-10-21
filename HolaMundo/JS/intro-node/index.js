const express = require('express')
const app = express()

app.get('*',(request,response)=>{
    response.send({ message: 'No entiendo na' })
})

app.listen(3000,()=>console.log('Servidor escuchando en puerto 3000'))