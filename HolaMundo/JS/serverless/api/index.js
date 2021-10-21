const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const cors = require('cors')

const app = express()
app.use(express.json())
app.use(express.urlencoded({
    extended: true
}))
app.use(cors())

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
app.get('*', (req,res)=>{
    res.setDefaultEncoding('Wenos dias')
})

module.exports = app