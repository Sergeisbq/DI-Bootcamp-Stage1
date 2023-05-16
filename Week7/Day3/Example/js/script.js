// console.log("hello from script")

/*

JS TYPES:
--------
1. Number
2. String
3. BooLean
4. Undefined
5. null



Numbers:
1
1.2
-1

Strings:
"1"
'2'

BooLean:
true // 1
false // 0

Undefined:
-


JS variables
------------
var
let (new in ECMAscript 6)
const (new in ECMAscript 6)

*/

// let a = 9;
// console.log(a);
// a = ttt;
// console.log(a);
// let name;
// console.log('name', name);


// const COLOR_BLACK = '#000000';
// b = 10;

// var c = null;
// var d;
// d='John';


// String methods
// let txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
// let len = txt.length;
// console.log(len);


// let str = "Please locate where 'locate' occurs!";
// let pos = str.lastIndexOf('locate');
// console.log(pos)


// let str = "Apple, Banan, Kiwi";
// let res = str.slice(7, 13);
// console.log(res);


// let str = "Apple, Banan, Kiwi";
// let res = str.substring(7, 2);
// console.log(res);


// let str = "Please visit Microsoft";
// let newStr = str.replace("Microsoft", "DevInst");
// console.log(newStr)


// let str = "Please visit Microsoft";
// let newStr = str.toUpperCase();
// console.log(newStr)
// let newStrL = str.toLowerCase();
// console.log(newStrL)


// let str = "Please visit!";
// let str1 = "Microsoft!";

// console.log(str + " " + str1);

// let str2 = str.concat(" " ,str1, " ", 'jhsgfhegrkffkhsjr');
// console.log(str2);

// let str3 = `${str} ${str1}`
// console.log(str3);


// let str = 'Hell World';
// console.log(str.charAt(0), str.charCodeAt(0));



// let addressNumber = 16;
// let addressStreet = 'Moshe Sharet';
// let country = 'Israel';
// let globalAddress = `I live in ${addressStreet} ${addressNumber}, in ${country}`;
// console.log(globalAddress);


// let str = "Hello World";
// let res = isNaN("1020");
// console.log(res);


// let x = 10;
// // let str = new String(x);
// let str = x.toString();
// console.log(str);


/*

JS COMPARISONS
--------------

==
!=
===
!==
>=
<=
>
<


*/


// alert('hello'); // Success message or error

// let res = prompt('Please enter a number'); // always string // getting data from user == input
// console.log(typeof res); // always string

// let res = confirm('Are you comingt to the party?'); // Boolean data
// console.log(res);



/*

JS DATA STRUCTURES
------------------

Array
Object

*/

// let arr = [2,'a','4',5,[1,2,3],6];
// arr[1] = 'b';
// arr[4][1] = 'c';
// console.log(arr);
// console.log(arr.length);


// let fruits = ["Banana", "Orange", "Apple", "Mango"];
// console.log(fruits.toString());
// console.log(fruits.join(', '))

// let str = 'abcdefg';
// console.log(str.split(''))


// let fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.push('Kiwi');
// console.log(fruits);
// last = fruits.pop();
// console.log(fruits);
// console.log(last);

// let some = fruits.unshift('kiwi');
// console.log(fruits);

// fruits[0] = 'bob';
// console.log(fruits);

// fruits[fruits.length] = 'Kiwi';
// console.log(fruits);

// fruits[fruits.length + 1] = 'Kiwi';
// console.log(fruits);

// fruits[100] = 'Kiwi';
// console.log(fruits.length);



// let myGirls = ['Cecilie', 'Lone'];
// let myBoys = ['Emil', 'Tobias', 'Linus'];
// let arr = [11, 11]

// console.log(myGirls.concat(myBoys, arr));


// let fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
// let slice = fruits.slice(3);
// console.log(slice); // slice doesn't change the original array, but splice changes
// console.log(fruits);


// let obj = {
//     a: 1,
//     b: 2,
//     name: "John",
//     arr: [1,2,3],
//     x: {a:10},
//     f: function(){
//         alert('hello')
//     }
// };
// let obj1 = new Object();

// obj.b = 20;
// console.log(obj)
// obj.y = 40;

// console.log(obj.x.a)
// console.log(obj['a'])
// console.log(obj['x'].a)
// console.log(obj['x']['a'])
// console.log(obj.f())

// delete obj.a
// console.log(obj)



// let obj = {
//     username: "John",
//     password: "1234567",
// };

// let obj1 = {
//     username: "Bob",
//     timeline: "123",
// };

// let database = [obj];
// let newsfeed = [obj1, obj1, obj1];

// console.log(obj);
// console.log(database);
// console.log(newsfeed);



/* 
JS CONDITIONALS
---------------

if
else if
else

switch
ternary operator
*/

// if(1 === '1'){
//     console.log('true');
// }
// else if('2' == '2'){
//     console.log('2');
// }
// else{
//     console.log('esle');
// }


// let page = 'none';
// switch (page) {
//     case 'home':
//         console.log('home');
//         break;
//     case 'shop':
//         console.log('shop');
//         break;
//     default:
//         console.log('404');
// }

// if(1==1){
//     console.log(1);
// }
// else{
//     console.log(2)
// }


// (1==1) ? console.log(1) : console.log(2);


// let x = (1==2) ? 1 : 'jdfhgk';
// console.log(x);


// let y = (1==2) ? 1 : (3==3) ? 3 : 4;
// console.log(y);


// let a = 2;
// let b = 2;
// let c = 5;

// if (a==b && b > c){
//     console.log(1);
// }
// else if ((a==c) && b > c){
//     console.log(2);
// }
// else{
//     console.log(3);
// }


/* 
LOOPS
-----

*/

let arr = ['a','b','c','d'];
// for(let i = 0; i < arr.length; i++) {
//     console.log(i, arr[i]);
// }

// for (let x in arr) {
//     console.log(x, arr[x]);
// }


// let obj = {
//     a:222,
//     b:333,
// }

// for (let y in obj) {
//     console.log(y, );
// }

// let x = 2;
// while (x < arr.length) {
//     x = x + 3;
//     console.log(x)
// }


let x = 0;
do{
    console.log('Do first this and check the condition');
    x++
}
while(x<0)











