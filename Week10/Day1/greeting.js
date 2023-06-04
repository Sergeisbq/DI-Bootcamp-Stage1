const greeting = (name) => {
    console.log(`Hello ${name}, welcome to NodeJS`);
}

const sayhello = (name) => {
    console.log(`Hello, ${name}`);
}

module.exports = {
    greeting, 
    sayhello // or a:sayhello and call a when call from another file
}