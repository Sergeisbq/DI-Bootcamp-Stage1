// function x() {
//     let x = 9;
//     console.log(x);
// }
// x();
// console.log(x);


// let x = 9;
// if (x < 10) {
//     x = 7;
// }
// else {
//     x = 5;
// }
// console.log(x);
// x = (x < 10) ? 7 : 5;


// let str = 'Hello';
// let str1 = 'student, please join the meet at the time, because it is make me crazy';
// let str2 = 'first thing in the morning';

// let str4 = str + " " + str1 + " " + str2;
// let str5 = `${str}
// ${str1}
// ${str2}`;
// console.log(str4);
// console.log(str5);

// function name_of_the_function(first_name = "Marry", last_name = "Gofer") {
//     console.log(first_name, last_name);
// }

// name_of_the_function("John", "Doe")

// const sum = function(x, y) {
//     return x + y;
// }


// const fullname = (x, y) => x + " " + y;
// console.log(fullname('yh', 'uy'));


// setTimeout(function() {
    
// }, 5000);

// setTimeout(() => {
    
// }, 500);



// let arr = ['a', 'b', 'c', 'd', 'e'];

// let len = arr.length;
// for (let i = 0; i < len; i++) {
//     console.log(arr[i]);
// }

// for (let i = len - 1; i >= 0; i--) {
//     console.log(arr[i]);
// }


// for (x of arr) {
//     console.log(x);
// }

// for (x in arr) {
//     console.log(x, arr[x]);
// }



//!!!
// forEach
// let arr = ['a', 'b', 'c', 'd', 'e'];
// arr.forEach( (item, index, arr) =>{

// })
// arr.forEach((item, i, arr2) => {
//     console.log(item, i);
//     arr2[i] = item + '#';
// })

// console.log(arr);


// const x = name => name;


//!!!
// some() every()

// let arr = ['a', 'b', 'c', 'd', 'e'];

// let even = arr.some((item) => {
//     return item === 'b';
// })

// console.log(even);

// let even2 = arr.every((item) => {
//     return item === 'a';
// })

// console.log(even2);


// let str = 'word in a given String';
// let words = str.split(' ');
// console.log(words);
// let arr = Array.from(str);
// console.log(arr);

// let arr2 = arr.join()

// for (let word of words) {
//     word = word.split('');
//     console.log(word);

//     for (let i in word, i = word.length -1, i--) {
//         let j = '';
//         j += i;
//         console.log(j);
//     }
// }



// function reverseWord(str) {
//     let ret = '';
//     for (let i = str.length - 1; i >= 0; i--) {
//         ret += str[i];
//     }
//     return ret
// }

// function reverseAll(str) {
//     let arr = str.split(' ');
//     arr.forEach((item, i, ret) => {
//         ret[i] = reverseWord(item)
//     });
//     return arr.join(' ');
// }

// let str = reverseAll('word in a given String')
// console.log(str);



// function x() {
//     let name = "Marry";
//     function y() {
//         console.log(name);
//     }
//     return y
// }
// x()();

// let a = x();
// console.log(a());


// function addSquardes(a, b) {
//     function square(x) {
//         return x * x
//     }
//     return square(a) + square(b)
// }

// let a = addSquardes(2, 3);
// console.log(a);


// function outside(x) {
//     function inside(y) {
//         return x + y;
//     }
//     return inside;
// }

// let a = outside(1.17);
// console.log(a);

// let b = a(20);
// console.log(b);

// b = a(40);
// console.log(b);


// const out = (x) => {
//     return (y) => {
//         return x + y
//     }
// }

// const vat = vat => y => vat * y;
// let vatis = vat(1.17);
// console.log(vatis(20));
// console.log(vatis(40));



// const x = (a, b) => c => {
//     return a(b(c));
// }

// const sum2 = num => num * 2;
// const sum = num => num + 1;

// let a = x(sum, sum2)(6);
// console.log(a);


// const y = a => b => a + b;

// const x = (a, b) => (c) => a(b(c));

// const sum2 = num => num * 2;
// const sum = num => num + 1;

// let a = x(sum, sum2)(6);
// console.log(a);


let a = 5;
b = a;
b++

console.log(a, b);

let arr1 = [1,2,3];
let arr2 = arr1;
let arr3 = [...arr1];
let arr4 = [].concat(arr1) // old method
arr2[1] = 5;
console.log(arr1);
console.log(arr2);
console.log(arr3);

let obj1 = {a:1, b:3, c:{d:4}};
let obj2 = obj1;
let obj3 = {...obj1}
let obj4 = Object.assign({}, obj1) // new method
obj1.c.d = 44;
console.log(obj1);
console.log(obj2);
console.log(obj3);
console.log(obj4);


let obj_1 = {a:1, b:3, c:{d:4}};
let str = JSON.stringify(obj_1);
let obj_2 = JSON.parse(str);

obj_1.c.d = 44;
console.log(str);
console.log(obj_1);
console.log(obj_2);








// function declaration

addition(2,4)


function addition (a, b) {
    return a + b
}

addition(2,4)

// function expression
// anonymous function

const addition_second = function (a,b) {
    return a + b
}

addition_second(2,4)



// callback function
div.addEventListener("click", function(){
    alert("hello")
})

// SELF INVOKING FUNCTION
// DECLARED AND EXECUTED AT THE SAME TIME

(function () {
    console.log("welcome")
})()

(function (username) {
    console.log("welcome" + username)
})("John")

// ARROW FUNCTION

function addition (a, b) {
    return a + b
}

const addition_third = function (a,b) {
    return a + b
}

const addition_fourth = (a, b) => a+b

function addition_fifth (a, b, operator) {
    if (operator === "+") {
        return a + b
    } else {
        return a - b
    }
}

const addition_six = (a, b, operator) => {
    let total = operator === "+" ? a + b : a - b
    return total
}

const addition_seven = (a, b, operator) => operator === "+" ? a + b : a - b

const winBattle = () => true
let experiencePoints = winBattle() ? 10 : 1