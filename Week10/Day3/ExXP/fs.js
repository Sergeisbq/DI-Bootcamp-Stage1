const fs = require('fs');

// -----1-----
// fs.readFile('text.txt', 'utf-8', (err, data) => {
//     if (err) {
//         console.log(err)
//         return
//     }
//     console.log(data);
// });

// -----2-----
// fs.writeFile('data.txt', 'utf-8', (err) => {
//     if (err) {
//         console.log(err)
//         return
//     }
//     else {
//         console.log('Operation complete');
//     }
// })

// -----3-----
// let newContent = "Hello from JS one more time";
// fs.appendFile('data.txt', newContent + '\n', (err) => {
//     if (err) {
//         console.error(err)
//         return
//     }
//     else {
//         console.log('Operation complete');
//     }
// });

// -----4-----
fs.unlink('data.txt', (err) => {
    if (err) {
        console.error(err)
        return
    }
    else {
        console.log('Operation complete');
    }
});