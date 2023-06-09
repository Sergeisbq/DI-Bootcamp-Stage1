const express = require('express');
const path = require('path')
const app = express();

const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.listen(3000, () => {
    console.log('server is running on port 3000');
})


app.get('/aboutMe/:hobby', (req, res) => {
    const hobby = req.params.hobby;
    const checkStr = /^([^0-9]*)$/;
    if (checkStr.test(hobby) === false) {
        return res.status(404).json({message: "Not relevant value"})
    }
    const obj = JSON.stringify({"hobby": hobby})
    console.log(obj);
    res.json(obj)
})


app.get('/pic', (req, res) => {
    res.send('<img src="https://wallpaperaccess.com/full/138728.jpg">')
})


app.use('/form', express.static(path.join(__dirname, 'public')))

app.post('/formData', (req, res) => {
    const email = req.body.email;
    const mes = req.body.message;
    res.send(`${email} sent you a message: '${mes}.'`);
})

