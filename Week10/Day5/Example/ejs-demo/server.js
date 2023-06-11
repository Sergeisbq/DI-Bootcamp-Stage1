const express = require('express');
const ejs = require('ejs');

const app = express();

// set template engine
app.set('view engine', 'ejs');

app.listen(process.env.PORT||3030, () => {
    console.log(`Run on ${process.env.PORT||3030}`);
})

app.get('/', (req, res) => {
    res.send('<h1>Hello EJS</h1>')
})
