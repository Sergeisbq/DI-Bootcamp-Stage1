const http = require('http');

const server = http.createServer((request, res) => {
    res.setHeader('Content-Type', 'text/html');

    res.end(`<h1>Hello from server</h1><br><h2>Hello from server</h2><br><h3>Hello from server</h3>`);
})

server.listen(3000, () => {
    console.log("I'm listening");
})