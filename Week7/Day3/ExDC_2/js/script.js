// ---1---

let x = 0;
let y = '*';
do
{
console.log(y);
y += '*';
x++;
}
while (x < 6);

// ---2---

let str = '';
for (let i = 0; i < 7; i += 1) {
    str = '';
    for (j = 1; j <= i; j += 1) {
        str += '*';
    }
    console.log(str)
}




