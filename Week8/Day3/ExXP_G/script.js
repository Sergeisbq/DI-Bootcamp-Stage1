// //-----1-----

// arr = [1, 2, 3]
// arr.map(num => {
//   if (typeof num === 'number') return num * 2;
//   return 
// });

// // [2,4,6]


// //-----2-----

// [[0, 1], [2, 3]].reduce(
//   (acc, cur) => {
//     return acc.concat(cur);
//   },
//   [1, 2],
// );
// // [1, 2, 0, 1, 2, 3]

// //-----3-----

// const arrayNum = [1, 2, 4, 5, 8, 9];
// const newArray = arrayNum.map((num, i) => {
//     console.log(num, i);
//     alert(num);
//     return num * 2;
// })
// // i - index


//-----4-----

// const array = [[1],[2],[3],[[[4]]],[[[5]]]];
// console.log(array.flat(2));

// const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]];
// let str = '';
// for (item of greeting.flat(1)) {
//     console.log(item);
//     str += `${item} `;
// }
// console.log(str);

// const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
// console.log(trapped.flat(Infinity));



// // XP_N

// const data = [
//   {
//     name: 'Butters',
//     age: 3,
//     type: 'dog'
//   },
//    {
//     name: 'Cuty',
//     age: 5,
//     type: 'rabbit'
//   },
//   {
//     name: 'Lizzy',
//     age: 6,
//     type: 'dog'
//   },
//   {
//     name: 'Red',
//     age: 1,
//     type: 'cat'
//   },
//   {
//     name: 'Joey',
//     age: 3,
//     type: 'dog'
//   },
//   {
//     name: 'Rex',
//     age: 10,
//     type: 'dog'
//   },
// ];

// let sum = data.reduce((total, item) => {
//     return total + (item.age * 7)
// }, 0)
// console.log(sum);


// const userEmail3 = ' cannotfillemailformcorrectly@gmail.com ';
// let str = userEmail3.trim();
// console.log(str);


// const users = [
//              { firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
//              { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
//              { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
//              { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
//              { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
//              { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
//              { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}
// ];

// const newUsers = users.reduce((acc, item) => {
//   const fullName = `${item.firstName} ${item.lastName}`;
//   acc[fullName] = item.role;
//   return acc;
// }, {});

// console.log(newUsers);


const letters = ['x', 'y', 'z', 'z'];

const newLetters = letters.reduce((acc, item) => {
  acc[item] = (acc[item] || 0) + 1;
  return acc;
}, {});

console.log(newLetters);
