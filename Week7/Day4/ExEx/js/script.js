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


/*
Exercise 1: Traversing the DOM
Knowing how to traverse the DOM using JavaScript provides a foundation
to altering an HTML page in real time.
Using the HTML markup in Listing 1, perform these tasks:
1. Use the firstElementChild property to access an element.
2. Use the lastElementChild property to access an element.
3. Use the nextElementSibling property to access an element.
4. Use the previousElementSibling property to access an element.
5. Use the parentNode property to access an element.
6. Use the childNodes property to access a group of child elements.
*/
console.log('Exercise 1: Traversing the DOM');
let elem = document.getElementById('content');
console.log(elem.firstElementChild);
console.log(elem.lastElementChild);
console.log(elem.firstElementChild.nextElementSibling);
console.log(elem.firstElementChild.nextElementSibling.previousElementSibling);
console.log(elem.firstElementChild.parentNode);
console.log(elem.childNodes);
/*
Exercise 2: Targeting nodes
In exercise 1, you learned how to target nodes in several ways.
Continuing to use the markup in Listing 1, perform the following tasks:
1. Retrieve the value of a node using / innerText / innerHTML / textContent.
2. Change the value of a node using / innerText / innerHTML. / textContent.
3. Retrieve the value of a node attribute.
4. Change the value of a node attribute.
*/
console.log('Exercise 2: Targeting nodes');
console.log(elem.firstElementChild.innerText);
console.log(elem.firstElementChild.textContent);
elem.firstElementChild.nextElementSibling.textContent = "Change the value of a node"
console.log(elem.getAttribute('id'));

/*
Exercise 3: Manipulating the DOM
Now that you know how to traverse the DOM and alter node values,
the next logical step is to learn how to add, remove, and replace nodes.
Perform the following tasks:
1. Use the appendChild method to add a node.
2. Use the insertBefore method to add a node.
3. Use the removeChild method to remove a node.
4. Use the replaceChild method to replace a node.
*/
let h2 = document.createElement('h2');
h2.innerText = 'added node'
elem.appendChild(h2)

let p = document.createElement('p');
p.innerHTML = "New paragraph element";
let content = document.getElementById('content');
content.insertBefore(p, content.firstChild);

document.getElementById('header').removeChild(document.getElementById('title'));

document.getElementById('content').replaceChild(content.firstElementChild, content.firstElementChild.nextElementSibling);


// let root = document.getElementById('root');
// let img = document.createElement('img');
// img.setAttribute('src', 'https://images.typeform.com/images/W7tvRFtpQn95');
// root.appendChild(img);