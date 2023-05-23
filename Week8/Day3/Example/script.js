// // Nested function

// function x() {
//     function y() {
//         return 1
//     }
//     return y
// }

// let sum = x()();
// console.log(sum);


// Compose

// const x = (a, b) => {
//     return (c) => {
//         return a(b(c));
//     }
// }

// // === const x = (a, b) => (c) => a(b(c));
// // const x = (sum, sum2) => {
// //     return (6) => {
// //         return sum(sum2(6)) === 13;
// //     }
// // }

// const sum2 = (num) => num * 2;
// const sum = (num) => num + 1;

// console.log(sum2(6));

// let total = x(sum, sum2)(6);


// Ternary operator

// let a = 5;
// let b = 5;
// // let c = '';

// if (a > b) {
//     c = 'haha';
// }
// else {
//     c = 'not haha';
// }

// // console.log(c); // == not haha

// let c = (a > b) ? 'haha' : (a === b) ? 'good' : 'not haha';
// console.log(c); // == not haha

//  Arrow function 

// function name(param1, param2) {

// }

// const name = function(param1, param2) {

// }

// const name = (param1, param2) => param1 + " " + param2;


// let arr = [1,2,3,4,5,6,7,8,9,0];

// for (let i = 0; i < arr.length; i++) {

// }

// for (x of arr) {

// }

// for (x in arr) {
    
// }

// arr.forEach((item, i, a) => {
//     console.log(item, i);
//     a[i] = item * 5;
// });



// // addevenetlistener with hover
// const span = document.getElementById('container');

// let color = '';

// span.addEventListener('mouseover', function(e) {
//     span.style.color = 'yellow';
// });

// span.addEventListener('mouseout', function(e) {
//     span.style.color = color;
// });


// // Object

// let last = 'lastname';
// let obj = {
//     name: 'Eil',
//     email: 'eli@gmail.com',
//     [last]: 'Joy',
// }

// console.log(obj.name);
// console.log(obj['lastname']);


// !!!!!
// let obj = {
//     username: '',
//     email: ''
// }

// function handleInput(e) {
//     obj[e.target.name] = e.target.value
//     console.log(obj);
// }


// let name = 'Alef';
// let email = 'alef@gmail.com';

// let user = {
//     name,
//     email,
// }

// console.log(user);



// // Includes

// const pets = ['cat', 'dog', 'bat'];

// let isDogExist = pets.includes('dog');
// let isDogExist2 = pets.includes('doG');
// console.log(isDogExist);
// console.log(isDogExist2);


// const str = '5';

// console.log(str.padStart(3, '0'));

// const creditCardNumber = '4580123454326482';

// creditCardNumberShort = creditCardNumber.slice(-4);
// console.log(creditCardNumberShort);
// console.log(creditCardNumberShort.padStart(creditCardNumber.length, '*'));
// console.log(creditCardNumberShort.padEnd(creditCardNumber.length, '*'));


// let str1 = '        aaaaa        ';
// console.log(str1);
// console.log(str1.trim());



// let arr = ['blue', ['red', ['yellow', 'orange']], 'green'];
// console.log(arr.flat(2)); // number is the level, 'infinity' - for all levels 

// let arr = [1,2,3,4]
// let arr3 = []
// arr2.forEach((item, i, arr) => {
//     arr3.push(item *2);
// })
// console.log(arr2);
// console.log(arr3);


// function map(arr) {
//     arr.forEach((item, i, arr) => {
//         arr[i] = item * 2;
//     });
//     return arr
// }
// console.log(map([1,2,3,4]));

// let arr = [1,2,3,4,5];

// let newArr = arr.map((item) => {
//     if (item !== 2) {
//         return item * 2
//     }
// })

// console.log(newArr);

// let arr = [0,1,1,2,3,5,8];

// function filter(arr) {
//     let ret = [];
//     arr.forEach((item, i) => {
//         if (item > 3) {
//             ret.push(item);
//         }
//     });
//     return ret
// }


// let filterArr = arr.filter((item) => {
//     return item > 3
// })
// console.log(filterArr);


// let arrN = [
//     {name: 'John', username: 'jjj'},
//     {name: 'Johny', username: 'jjjj'},
//     {name: 'Johana', username: 'jjjjj'},
//     {name: 'Marry', username: 'mmm'},
// ]

// // let filterArr = arrN.filter((item) => {
// //     if (item.username[0] == 'j') {
// //         return item
// //     }
// // })
// // console.log(filterArr);

// let filterArr = arrN.filter((item) => {
//     return item.name.toLowerCase().startsWith('jo') | item.username.toLowerCase().includes('b'); // includes('a');
// })
// console.log(filterArr);


// let arr1 = [2, 5, 10, 100];

// function reduce(arr) {
//     let sum = 0;
//     arr.forEach((item, i) => {
//         sum += item;
//     });
//     return sum
// }
// console.log(reduce(arr1));

// let sum = arr1.reduce((total, item) => {
//     return total + item
// }, 1000)
// console.log(sum);

let newVal = 0;
const a = function(num) {
    numstr = String(num);
    if (numstr.length > 1) {
        for (i in numstr) {
            newVal += parseInt(numstr[i])
            if (newVal > 10) {

            }
        }
        
    }
    
}

a(16);


// // !!!!!!
// function calcDigit(num) {
//     let arr  = new String(num).split('');
//     let sumOfDigits = arr.reduce((total, num) => {
//         return total + Number(num);
//     }, 0)
//     return (sumOfDigits < 10) ? sumOfDigits : calcDigit(sumOfDigits)
// }
// console.log(calcDigit(4931934)); 



function calcDigit2(num) {
    let arr  = new String(num).split('');
    let sumOfDigits = 0;
    for (i in arr) {
        sumOfDigits += Number(arr[i]);
    }
    return (sumOfDigits < 10) ? sumOfDigits : calcDigit2(sumOfDigits)
}
console.log(calcDigit2(4931934)); 