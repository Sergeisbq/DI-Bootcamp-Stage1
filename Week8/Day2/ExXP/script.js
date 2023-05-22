
// //-----1-----
// // #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne() // // Answer - a = 3
// // #1.2 What will happen if the variable is declared 
// // with const instead of let ? // Answer - a = 5


// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree() // Answer is 0
// funcTwo() // Answer is nothing, just change the a value
// funcThree() // Answer is 5
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ? // An Error when call the funcTwo()


// //#3
// function funcFour() {
//     window.a = "hello";
// }

// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour() // Nothing??
// funcFive() // a = 5


// //#4
// let b = 1;
// function funcSix() {
//     let b = "test";
//     alert(`inside the funcSix function ${b}`);
// }

// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ? // Nothing, because we have let b inside the function and b equal to the 'test'


// //#5
// let c = 2;
// if (true) {
//     let c = 5;
//     alert(`in the if block ${c}`);
// }
// alert(`outside of the if block ${c}`);

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ? // Nothing changes because the same as Number 4


// //-----2-----
// const winBattle = () => true 
// let experiencePoints = winBattle() ? 10 : 1; 
// console.log(experiencePoints);


// //-----3-----
// const isString = (a) => {
//     if (typeof a == 'string') {
//         return true
//     }
//     else {
//         return false
//     }
// }
// let a = isString(10);
// console.log(a);


// //-----4-----
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// colors.forEach( (item, i, arr) => {
//     console.log(`${i+1}# chioce is ${item}`);
// })

// let violet = colors.some((item) => {
//     if (item === 'Violet') {
//         return console.log('Yeah');
//     }
// })


// //-----5-----
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// const ordinal = ["th","st","nd","rd"];
// colors.forEach( (item, i, arr) => {
//     if (i == 0) {
//         console.log(`${(i+1)+ordinal[1]}# chioce is ${item}`);
//     }
//     else if (i == 1) {
//         console.log(`${(i+1)+ordinal[2]}# chioce is ${item}`);
//     }
//     else if (i == 2) {
//         console.log(`${(i+1)+ordinal[3]}# chioce is ${item}`);
//     }
//     else {
//         console.log(`${(i+1)+ordinal[0]}# chioce is ${item}`);
//     }
// })


// //-----6-----
let bankAmount;
let vat_s = 1.17;
let summ = 8000;
const details = ["+200", "-100", "+146", "+167", "-2900"];
details.forEach((item, i, arr) => {
    let new_item = parseInt(item) * vat_s;
    summ += new_item;
    console.log(summ);
    // if (item[0] == '+') {
    //     console.log(item[0]);
    //     item = item.replace('+', '-');
    //     console.log(parseInt(item));
    // }
    // else if (item[0] == '-') {
    //     console.log(item[0]);
    //     item = item.replace('-', '+');
    //     console.log(parseInt(item));
    // }
})


