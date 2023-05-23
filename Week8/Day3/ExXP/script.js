// //------1------
// //------1.1------
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits]; // ['bread', "carrot", "potato", 'chicken', "apple", "orange"]
// console.log(result);

// //------1.2------
// const country = "USA";
// console.log([...country]); // ['U', 'S', 'A']

// //------Bonus------
// let newArray = [...[,,]];
// console.log(newArray); // [undefined, undefined]


// //------2------
// //------2.1------
// const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
//              { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
//              { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
//              { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
//              { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
//              { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
//              { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}
// ];

// let welcomeStudents = []
// function map(arr) {
//     arr.forEach((item, i, arr) => {
        
//         item.firstName = `Hello ${item.firstName}`;
//         welcomeStudents.push(item.firstName)
//     });
//     return welcomeStudents
// }
// console.log(map(users));

// //------2.2------
// let onlyFS = [];
// let filterArr = users.filter((item) => {
//     if (item.role == 'Full Stack Resident') {
//         onlyFS.push(item);
//         return onlyFS
//     }
// })
// console.log(filterArr);

// //------2.3------


// //------3------
// const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
// let str = '';
// function reduce(arr) {
//     arr.forEach((item, i) => {
//         str += `${item} `;
//     });
//     return str
// }
// console.log(reduce(epic));

// //------4------
const students = [
               {name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}
];

let studentsPass = [];
let filterArr = students.filter((item) => {
    if (item.isPassed == true) {
        studentsPass.push(item);
        return studentsPass
    }
})

studentsPass.forEach((item, i, arr) => {
    let sentense = '';
    sentense = `Good job ${item.name}, you passed the course in ${item.course}`;
    return console.log(sentense);
})

console.log(filterArr);