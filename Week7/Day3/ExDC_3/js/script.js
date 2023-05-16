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