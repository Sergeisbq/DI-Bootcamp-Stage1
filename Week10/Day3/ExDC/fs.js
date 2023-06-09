const fs = require('fs');

let sum = 0; 
let pos = 0; 
let flag = false;

fs.readFile('RightLeft.txt', 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    for (const item of data) {
        sum++
        if (item == '>') {
            pos++;
        }
        else if (item == '<') {
            pos--;
        }

        if (pos == -1 && flag == false) {
            console.log(`For pos -1 needed ${sum} steps`);
            flag = true;
        }
    }
console.log(`Final position at the end of the file is ${pos} steps to the right.`);    
});

