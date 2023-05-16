// ---1---

let numbers = [123, 8409, 100053, 333333333, 7]

for (x in numbers) {
    if (numbers[x] % 3 == 0) { 
        console.log(numbers[x]);
        console.log(numbers[x] / 3, true);
      }
    else if (numbers[x] % 3 != 0) { 
        console.log(numbers[x]);
        console.log(numbers[x] / 3, false);
      }
}


// ---2---

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let res = prompt('Please enter a name').toLowerCase();
if (res in guestList) {
    let sentense = `Hi! I'm ${res}, and I'm from ${guestList[res]}.`;
    console.log(sentense);
}
else {
    let sentense = `Hi! I'm a guest.`;
    console.log(sentense);
}


// ---3---

let age = [20,5,12,43,98,55];

let y = 0;
for (x in age) {
    y += age[x];
}
console.log(y);

let z = age[0];
for (let i = 0; i < age.length; i++) {
    if (z < age[i]) {
        z = age[i];
    }
}
console.log(z);
