// // -----1-----
// let a = 0;
// let arr2 = [1, 2, 3, 4, 5];
// arr2.forEach((item, i, arr) => {
//     a += item;
// })
// console.log(a);


// // -----2-----
// let arr2 = [1, 2, 3, 4, 5, 2];
// let arr3 = [];
// arr2.forEach((item, i, arr) => {
//     if (item in arr3) {
//         arr2.pop(item);
//     }
//     else {
//         arr3.push(item);
//     }

// });

// console.log(arr2);
// console.log(arr3);


// // -----3-----
// let arr4 = []
// let sample_arr = [NaN, 0, 15, false, -22, '',undefined, 47, null];
// sample_arr.forEach((item, i, arr) => {
//     if (typeof item == 'number' && !isNaN(item) && item !== 0) {
//         arr4.push(item);
//     }
// });

// console.log(sample_arr);
// console.log(arr4);


// // -----4-----
const repeat = (a, b) => {
    let output = '';
    for (let i = 0; i < b; i++) {
        output += a;
    }
    return output
}
console.log(repeat('Ha!', 5));


// // -----5-----
