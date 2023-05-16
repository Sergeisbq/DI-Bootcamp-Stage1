// ---1.1---

const people = ["Greg", "Mary", "Devon", "James"];

people.shift("Greg");
people[2] = 'Jason';
people.push('Sergei');
console.log(people.indexOf("Mary"));
let res = people.slice(1, 3);
console.log(res);
console.log(people.indexOf("Foo"));
const last = people[people.length - 1] 
console.log(last);

console.log(people);


// ---1.2---

for (let x in people) {
    console.log(people[x]);
}

for (let x in people) {
    if (people[x] == 'Devon') { 
        break;
      }
    console.log(people[x]);
}

// ---2---

const colors = ["Black", "Green", "White", "Beige", "Grey"];
const suffixes = ["1st", "2nd", "3rd", "4th", "5th"];

for (let x in colors) {
    let sentense = `My ${suffixes[x]} choice is ${colors[x]}`;
    console.log(sentense);
}

// ---3---

let j = 0;
do
{
let i = parseInt(prompt('Please enter a number'));
j = i + j;
console.log(j)
}
while (j < 10);

// ---4---

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);
let tenant = building.nameOfTenants[1].toLowerCase() //"Dan"

if((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent[tenant][1]){
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log(building.numberOfRoomsAndRent.dan)

// ---5---

let family = {
    mom: 31,
    dad: 32,
    kid: 1,
}

for (const x in family) {
    console.log(`${x}`);
}
console.log(Object.keys(family));

for (let x in family) {
    console.log(family[x]);
}
console.log(Object.values(family));


// ---6---

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}
let str = '';
for (const x in details) {
    str += `${x} ${details[x]} `;
}
console.log(str);


// ---7---

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let str1 = '';
for (const x in names.sort()) {
    let letter = names[x].charAt(0);
    str1 += letter;
}
console.log(str1);
