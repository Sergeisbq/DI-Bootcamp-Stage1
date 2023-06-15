const express = require('express');
const app = express();

app.use(express.urlencoded({extended:true}));
app.use(express.json())

app.listen(3030, () => {
    console.log('3030');
})

app.get('/tlv/:a', (req, res) => {
    req.body
    res.send('Hello TLV greeting all ' + req.query.a + " " + req.query.b)
})