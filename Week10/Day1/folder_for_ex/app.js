// let a = 666;
// let b = 6;

// console.log(a + b);

const http = require('http');

const server = http.createServer((request, response) => {
    response.end('Hello from the server')
})

server.listen(6000, () => {
    console.log('run on 7000');
})