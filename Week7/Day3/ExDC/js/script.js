// ---1---

let str = "The movie is not that bad, I like it";
let str1 = str.replace(',', '');
console.log(str1);
const usingSplit = str1.split(' ');

console.log(usingSplit);
let wordNot = usingSplit.indexOf("not");
console.log(wordNot);
let wordBad = usingSplit.indexOf("bad");
console.log(wordBad);

usingSplit.splice(wordNot, wordBad - wordNot + 1, 'good');
console.log(usingSplit);
let str2 = usingSplit.toString();
console.log(str2);
let str3 = str2.replaceAll(',', ' ');
console.log(str3);




// console.log(str2.replace(',', ' '));


// let wordNot = 0;
// for (x in usingSplit) {
//     if (usingSplit[x] == 'not') {
//         break;
//     }
//     console.log(usingSplit[x]);
//     wordNot = parseInt(x) + 1;
// }
// console.log(wordNot);

// let wordBad = 0;
// for (x in usingSplit) {
//     if (usingSplit[x] == 'bad') {
//         break;
//     }
//     console.log(usingSplit[x]);
//     wordBad = parseInt(x) + 1;
// }
// console.log(wordBad);




