const {largeNumber} = require('./main.js');
const {currentdate} = require('./main.js')

const b = 5;
const result = largeNumber + b
console.log(result);

const http = require('http');

// const server = http.createServer((request, res) => {
//     res.setHeader('Content-Type', 'text/html');

//     res.end(`<p>My Module is: <br>${result}</p><br><h1>Hi there at the frontend</h1>`);
// })

const server = http.createServer((request, res) => {
    res.setHeader('Content-Type', 'text/html');

    res.end(`<h1>The date and time are currently: ${currentdate}</h1>`);
})

server.listen(3000, () => {
    console.log("I'm listening");
})