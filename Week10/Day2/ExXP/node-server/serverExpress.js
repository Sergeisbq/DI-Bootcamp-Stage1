const express = require('express');
const app = express();

app.listen(3000, () => {
    console.log('server is running on port 3000');
})

app.get('/api/pruducts', (req, res) => {
    res.send('<h1>Hello World</h1><br><h2>Hello World</h2><br><h3>Hello World</h3>');
})