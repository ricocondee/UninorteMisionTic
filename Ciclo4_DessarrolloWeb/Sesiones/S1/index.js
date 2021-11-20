/*
Antes de correr el programa, por favor ejecutar npm install express
*/
const path = require('path')        // Incluye el módulo path, para manejo de diectorios
const express = require('express')  // Framework 

const app = express()               // app = Flask(__name__)
app.use(express.json())

app.get('/', (pet, res) => {        // @app.route('/')
    res.sendFile(path.join(__dirname, 'index.html'))
})

app.post('/suma', (pet, res) => {   // @app.route('/suma', methods=['POST'])
    const {a, b} = pet.body
    let result = parseInt(a)+parseInt(b)
    res.send({result:result})
    console.log(result)
})

app.listen(5000, () => {            // app.run(5000)
    console.log("Servidor escuchando por el puerto 5000")
})