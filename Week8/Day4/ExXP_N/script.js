class Bird {
    constructor() {
      console.log("I'm a bird. 🦢");
    }
}
  
class Flamingo extends Bird {
    constructor() {
      console.log("I'm pink. 🌸");
      super();
    }
}
  
const pet = new Flamingo(); // Answer - "I'm pink. 🌸" /n "I'm a bird. 🦢"




// let arr1 = [2,4,4,1];

// function bCC(arr) {
//     let amount = 0;
//     arr.forEach((item) => {
//         if (item >= 4)
//         amount += 1;
//         return amount
//     });
//     console.log(amount); 
// }

// bCC(arr1);


// let arr = [2,4,4,1];


// function birthdayCakeCandels(arr) {
//     let maxNum = Math.max(...arr);
//     let filter = arr.filter(value => {
//         return value === maxNum
//     })
//     // console.log(filter);
//     return filter.length;
// }

// let how_many = birthdayCakeCandels(arr);
// console.log(how_many);


// let arr_f = [2,5,3,7,2,3,6,8,6];
// let arr_n = []
// function smalestDist(arr) {
//     for (i in arr) {
//         arr_n.push(arr[i]);
//         i += 1;
//         if (i+1 !== i) {
//             arr_n.push(arr[i])
//         }
//     }
//     console.log(arr_n); 

//     }

// smalestDist(arr_f)



// let arr = [2,5,3,7,2,3,6,8,6];

// function minimumDistances(a) {
//     let distances = [];
//     for (let i = 0; i < a.length; i++) {
//         if (a.indexOf(a[i]) !== a.lastIndexOf(a[i])) {
//             let minDistance = a.lastIndexOf(a[i]) - a.indexOf(a[i]);
//             distances.push(minDistance);
//         }
//     }
//     return (distances.length === 0) ? -1 : distances.sort()[0]
// }

// let smallest = minimumDistances(arr)
// console.log(smallest);



// Array Destructuring

// let arr = [2,5,3,7,2,3,6,8,6];

// // const a = arr[0];
// // const b = arr[1];
// // ===

// const [a, b, c] = arr;

// console.log(b);


// Array Spreading

// let a = 1;
// let b = 2;
// let arr2 = [5,6,7];
// let arr3 = [a, ...arr2, b];

// console.log(arr3);


// Array Rest parameters

// let arr = [2,5,3,7,2,3,6,8,6];
// const [a, b, c, ...rest] = arr;
// console.log(a, b, c, rest);

// function x([a,b, ...rest]) {
//     console.log(a);
//     console.log(b);
//     console.log(rest);
// }

// x(arr)



// // Object method

// const population = {
//     tokyo: 37833000,
//     delhi: 24953000,
//     shanghai: 22991000,
// }

// for (i in population) {
//     console.log(i, population[i]);
// } 

// // Object.keys
// console.log(Object.keys(population));
// Object.keys(population).forEach((item, i) => {
//     console.log(item);
// });

// // Object.values
// console.log(Object.values(population));
// Object.values(population).forEach((item, i) => {
//     console.log(item);
// });

// // Object.entries
// console.log(Object.entries(population));
// Object.entries(population).forEach((item, i) => {
//     console.log(item);
// });
// // ===
// console.log(Object.entries(population));
// Object.entries(population).forEach(([key, value], i) => { // === [key, value] = [a, b]
//     console.log(key, value);
// });


// Object Distructuring

// const population = {
//     tokyo: 37833000,
//     delhi: 24953000,
//     shanghai: 22991000,
// }

// const {shanghai, tokyo, delhi} = population;
// console.log(tokyo, delhi, shanghai);


// Object Spreading

// const population = {
//     tokyo: 37833000,
//     delhi: 24953000,
//     shanghai: 22991000,
// }

// let obj2 = {
//     tokyo: 4444,
// }

// const obj3 = {...population, tokyo: 0, telaviv: 22367000}
// console.log(obj3);

// const obj3 = {...population, ...obj2} // if keys of objects are equal, new object gets value from the last object
// console.log(obj3);

// let {tokyo} = population;
// let population_tokyo = tokyo;
// let {tokyo} = obj3;
// console.log(population_tokyo, tokyo);



// Classes

// class NameOfClass {
//     constructor(param1, param2) {
//         this.name = 'John';
//         this.surname = param1;
//         this.birthday = param2;
//     }
//     getName() {
//         return this.name + this.surname + this.birthday
//     }
//     setA(param){
//         this.name = param
//     }
// }

// let abc = new NameOfClass('c', 'd');
// let bca = new NameOfClass('r', 't');
// bca.setA('z')
// console.log(abc.getName());
// console.log(bca.getName());


// class Animal {
//     #name
//     constructor(name) {
//         this.#name = name;
//     }
//     speak() {
//         console.log(`${this.#name} makes a noise`);
//     }
// }

// class Dog extends Animal {
//     constructor(name, color) {
//         super(name);
//         this.color = color;
//     }
//     speak() {
//         console.log(`${this.name} ${this.color} bark`);
//     }
//     getColor() {
//         return this.color
//     }
// }

// class Cat extends Animal {
//     constructor(name, color) {
//         super(name);
//     }
//     speak() {
//         console.log(`${this.name} meow`);
//     }
//     getColor() {
//         return this.color
//     }
// }

// class Frenchi extends Dog {
//     constructor(name, color, type) {
//         super(name, color);
//         this.type = type;
//     }
//     getName() {
//         return this.name
//     }
// }

// const dog = new Dog('Buddy', 'black');
// dog.speak()

// const dog1 = new Dog('Archi', 'white');
// dog1.speak()

// const fr = new Frenchi ('Rex', 'Brown', 'Frenchi');
// fr.getColor();
// fr.speak();
// fr.name = 'Rexie1';
// console.log(fr.name);

// const dog = new Animal('Dog');
// dog.speak()

// const cat = new Animal('Cat');
// cat.speak()
