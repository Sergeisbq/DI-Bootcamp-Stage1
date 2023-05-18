console.log("We start the song at 99 bottles");

let bottles = 99;
do
{
    let answer = parseInt(prompt("Type the new number of bottles"));
    let res = parseInt(answer);

    if (res == 1) {
        bottles -= res;
        console.log(`Take _${res}_ down, pass it around`);
        console.log(`we have now ${bottles} bottles`);
    }

    else if (res >= 2 && res <= 99){
        bottles -= res;
        console.log(`Take _${res}_ down, pass them around`);
        console.log(`we have now ${bottles} bottles`);
    }

    else {
        alert("It's not a number, please try again");
        continue
    }
}
while (bottles > 0);