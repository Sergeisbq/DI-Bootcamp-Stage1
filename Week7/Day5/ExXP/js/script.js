function playTheGame() {
    let answer = confirm("Would you like to play the game?");
    if (answer == true) {
        let userNumber = parseInt(prompt("Type the number from 0 to 10"));
        if (userNumber <= 10 && userNumber >= 0) {
            let computerNumber = Math.round(Math.random()*(10 - 1)+1);
            compareNumbers(userNumber, computerNumber);
        }
        else if (userNumber > 10 || userNumber < 0) {
            alert("Sorry it's not a good number, please try again");
        }
        else {
            alert("Sorry Not a number, Goodbye");
        }
    }
    else {
        alert("No problem, Goodbye");
    }
    
}

function compareNumbers (num1, num2) {
    for (let counter = 0; counter < 2; counter++) {
        console.log(counter);
        if (num1 === num2) {
            alert("WINNER");
            break
        }
        else if (num1 > num2 || num1 < num2) {
            alert("Your number is bigger or smaller then the computer's, guess again");
            num1 = parseInt(prompt("Type the new number from 0 to 10"));
            continue
        }
    }
}











