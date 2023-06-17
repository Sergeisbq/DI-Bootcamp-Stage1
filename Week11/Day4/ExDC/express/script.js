const express = require('express');
const app = express();
const cors = require('cors');

app.use(cors());

app.use(express.urlencoded({extended:true}));
app.use(express.json())

app.get("/api/hello", (req, res) => {
    res.send("Hello From Express");
})

app.post("/api/world", (req, res) => {
    res.send({message: `I received your POST request. This is what you sent me: ${req.body.message}`});
    
})

app.listen(3030, () => {
    console.log("Listening on 3030 port");
})