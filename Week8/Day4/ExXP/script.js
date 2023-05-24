
// // -----1-----
// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }

// const {name, location: {country, city, coordinates: [lat, lng]}} = person;

// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);
// // Answer - I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207).


// // -----2-----
// function displayStudentInfo(objUser){
//     const {first, last } = objUser;
//     console.log(`Your full name is ${first} ${last}`);
// }

// displayStudentInfo({first: 'Elie', last:'Schoppik'});


// // -----3-----
// const users = {user1: 18273, user2: 92833, user3: 90315};
// const newArr = [];
// Object.entries(users).forEach(([key, value], i) => {
//         newArr.push([key, value * 2]);
//     });
// console.log(newArr);


// // -----4-----
// class Person {
//     constructor(name) {
//       this.name = name;
//     }
//   }
  
//   const member = new Person('John');
//   console.log(typeof member); 
// // Answer - Object.


// // -----5-----
// class Dog {
//     constructor(name) {
//       this.name = name;
//     }
// };

// // This one will successfully extend the Dog class:
// class Labrador extends Dog {
//     constructor(name, size) {
//       super(name);
//       this.size = size;
//     }
// };


// // -----6-----
const x = function() {
    if ([2] !== [2]) {
        return console.log('Hi');
}
}
x() // Answer - false

const y = function() {
    if ({} !== {}) {
        return console.log('Hello');
}
}
y() // Answer - false


const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number) // Answer - 4
console.log(object3.number) // Answer - 4
console.log(object4.number) // Answer - 5

class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

class Mamal extends Animal {
    constructor(name, type, color) {
        super(name, type, color);
    }
    sound(param) {
        console.log(`${param} I'm a ${this.type}, named ${this.name} and I'm ${this.color} `);
    }
}

const farmerCow = new Mamal('Lily', 'cow', 'brown and white');
farmerCow.sound('Moooo')
