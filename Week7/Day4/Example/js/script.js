// let b = 3, d = b, u = b;

// const tree = ++d * d*b * b++ +
//  + --d+ + +b-- +
//  + +d*b+ +
//  u

// console.log(tree);

// b = 3, d = 3, u = 3
// ++d = 4
// d*b = 4*3
// b++ = 3
// --d = 3
// b-- = 4
// d = 3
// b = 3
// u = 3

// 4 * 4 * 3 * 3 + // 144
//  + 3+ + +4 + // 151
//  + +3*3+ + // 160
//  3 // 163


// let a = 6;
// {
//     var i = 9;
// }
// console.log(i)
// let b = 5;
// const D = 7;

// getName('Marry', 'John')  // doesn't matter where you call the fuction

// function getName(param1, param2) {
//     console.log(param1, param2);
// }



// function getFullName(a, b = "Doe")  {
//     console.log(a + " " + b);
// }
// getFullName('Marry')

// let c = 10;
// function getAge(a, b)  {
//     let c = 15;
//     // console.log((a * b) + c);
//     return ((a * b) + c)
// }
// console.log(c);

// let age = getAge(3, 5);
// console.log(age);



// function myAge(a)  {
//     console.log(`My mom is ${a * 2} years old and my dad is ${a * 2 * 1.2} years old`);
// }
// myAge(32);

// function myAge(a)  {
//     return(a * 2);
// }
// momAge = myAge(32);
// console.log(momAge);



// function getAge() {
    
// }

// const age = function() {
//     return '70';
// }
// console.log(age());


// const age1 = () => '75';
// console.log(age1());


// const x = (a,b) => a * b;
// console.log(x(2,3));


// Object method

// let pokemon = {
//     firstname: 'Pika',
//     lastname: 'Chu',
//     fullname: function() {
//         return this.firstname + this.lastname
//     }
// }

// let pikachu = pokemon.fullname();
// console.log(pikachu);



// var x = 5;
// function foo() {
//     var x = 1;
//     console.log(this.x);
// }
// foo()

// let obj = {
//     x: 2,
// }

// obj.a = foo;
// console.log(obj);

// console.log(obj.a());


// var name = 'John';
// function getName() {
//     return this.name
// }

// console.log(getName());

// let obj = {
//     name: 'Marry',
//     getName: getName,
// }

// console.log(obj.getName());


// ------DOM------ Document Object Model

// let div = document.getElementById('outerdiv');
// console.log(div.children[1]);
// console.log(div.firstElementChild);
// console.log(div.lastElementChild);
// console.log(div.parentNode);

// console.log(div);
// console.log(div.getAttribute('class'));

// let div = document.getElementsByTagName('div');
// console.log(div[0], div[1]);


// let divs = document.getElementsByClassName('a');
// let h1 = divs[1];
// h1.innerText = 'Learning DOM';
// h1.textContent = 'DOM Manipulation';
// h1.innerHTML = '<span style="color:red"> I am red </span>';


// console.log(div);

// console.log(divs[1]);

// let div = document.querySelector('#outerdiv.a .b');



let root = document.getElementById('root');
let img = document.createElement('img');
img.setAttribute('src', 'https://images.typeform.com/images/W7tvRFtpQn95');
root.appendChild(img);