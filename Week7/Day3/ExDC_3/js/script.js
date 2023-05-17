// ---1---

const numbers = [5,0,9,1,7,4,2,6,3,8];

let flag;
do
{
flag = false;
for (let i = 0; i < numbers.length - 1; i++) {
    
    if (numbers[i] < numbers[i + 1]) {
        [numbers[i], numbers[i + 1]] = [numbers[i + 1], numbers[i]];
        flag = true;
    }
  }
}
while(flag);
console.log(numbers);




// const arr = [5,0,9,1,7,4,2,6,3,8];
// console.log(arr.toString());

// for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < arr.length; j++) {
//         if(arr[i] < arr[j]) {
//             let temp = arr[i];
//             arr[i] = arr[j];
//             arr[j] = temp;
//         }

//     }
    
// }
// console.log(arr.toString());