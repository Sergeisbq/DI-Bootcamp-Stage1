const express = require('express');
const cors = require('cors')
const path = require('path')
const app = express();



app.use(cors())

const user = {
    firstname: 'John',
    lastname: 'Doe'
}

app.listen(3000, () => {
    console.log('server is running on port 3000');
})

// app.get('/', (req, res) => {
//     console.log("heyy");
//     res.json(user)
//     // res.send(user)
// })

app.get('/:id', (req, res) => {
    const id = req.params.id;
    const obj = JSON.stringify({"id": id})
    console.log(obj);
    res.json(obj)
})


app.use(express.static(path.join(__dirname, 'public')))
// app.use(express.static(path.join(__dirname, 'css')))
// app.use(express.static('public'));
app.get('/', (req, res) => {
    // console.log("heyy");
    // res.json(user)
    // res.send(user)
})
