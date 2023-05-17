// //-----1-----

// const arr = [];
// for (let i = 0; i <= 500; i++) {
//     arr.push(i);
// }
// console.log(arr);

// let a = [];
// function isDivisible(divisor) {
//     for (let item of arr) {
//         if (item % divisor == 0) {
//             a.push(item);
//         }
//     }
//     return a
// }

// let b = isDivisible(23)
// console.log(b);

// let c = 0;
// for (x in b) {
//     c += b[x];
// }
// console.log(c);


// //-----2-----

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let shoppingList = ["banana", "orange", "apple"];
// let a = 0;
// function myBill() {
//     for (i in shoppingList) {
//         if (shoppingList[i] in stock && stock[shoppingList[i]] > 0) {
//             stock[shoppingList[i]] -= 1;
//             console.log(stock[shoppingList[i]]);
//             if (shoppingList[i] in prices) {
//                 a += prices[shoppingList[i]];
//             }
//         }
//     }
//     return a
// }

// let b = myBill()
// console.log(b);


// //-----3-----

// function changeEnough(itemPrice, amountOfChange) {
//     if ((amountOfChange[0] * 0.25 + amountOfChange[1] * 0.1 + amountOfChange[2] * 0.05 + amountOfChange[3] * 0.01) > itemPrice) {
//         return true;
//     }
//     else {
//         return false;
//     }
// }
// a = changeEnough(0.75, [0,0,20,5]);
// console.log(a);


// //-----4-----

// function hotelCost() {
//     do
//     {
//     res = parseInt(prompt('Type the number of nights'));
//     }
//     while (isNaN(res) || res == 0);
//     return res * 140;
// }

// function planeRideCost() {
//     res = prompt('Type the destination');
//     if (res == 'London') {
//         return 183;
//     }
//     else if (res == 'Paris') {
//         return 220;
//     }
//     else {
//         return 300;
//     }
// }

// function rentalCarCost() {
//     do
//     {
//     res = parseInt(prompt('Type the number of days'));
//     }
//     while (isNaN(res) || res == 0);
//     if (res > 10) {
//         return (res * 40) * 0.95;
//     }
//     else {
//         return res * 40;
//     }
// }

// function totalVacationCost() {
//     a = hotelCost();
//     b = planeRideCost();
//     c = rentalCarCost();
//     let sentense = `The car cost: ${c}, the hotel cost: ${a}, the plane tickets cost: ${b}`;
//     console.log(sentense);
// }

// d = totalVacationCost();
// console.log(d);


// // -----5-----
// // ----5.2----
// let div = document.getElementById('container');
// console.log(div);

// let ul = document.getElementsByClassName('list');
// console.log(ul[0]);

// let li = ul[0].lastElementChild;
// li.textContent = 'Richard';

// let liS = ul[1].firstElementChild.nextElementSibling;
// liS.remove();

// let fmn = document.getElementsByTagName('li');
// for (i in fmn) {
//     fmn[i].textContent = 'Sergei';
// }

// //----5.3----
// for (let item of ul) {
//     item.classList.add("student_list");
// }
// console.log(ul);

// ul[0].classList.add("university", "attendance");
// console.log(ul);

// //----5.4----
// div.style.backgroundColor = "lightblue";
// div.style.padding = "10px";

// uls = ul[0].firstElementChild;
// uls.style.display = 'none';

// ula = ul[0].lastElementChild;
// ula.style.border = '3px solid black';

// let body = document.body;
// body.style.fontSize = '20px';


// //-----6----- next file









