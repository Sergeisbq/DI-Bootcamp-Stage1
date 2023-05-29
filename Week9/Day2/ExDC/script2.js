//-----2-----

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

const toJs = () => {
return new Promise((res, rej) => {
    let morseObj = JSON.parse(morse);
    if (Object.keys(morseObj).length > 1) {
        res(morseObj)
    }
    else {
        rej('Error, empty object')
    }
    })
}

toJs()
.then(res => {
    let r = toMorse(res);
    console.log(r);
})
.catch(err => {
    console.log(err);
})

  
let userInpU;
const toMorse = (morseObj) => {
    return new Promise((res, rej) => {
        let userInp = prompt('Type a word or sentense').toLowerCase();
        let toCompare = userInp.split('');
        let letters = Object.keys(morseObj);
        let arrA = [];
        userInpU = userInp.toUpperCase();
        for (let item of toCompare) {
            if (letters.includes(item)) {
                arrA.push(morseObj[item])
            }
            else {
                rej('Error, unknown charackter')
                break
            }
        }
        res(arrA);
        joinWords(arrA)
    })
}


const joinWords = (morseTranslation) => {
    let div = document.getElementById('root');
    let h3 = document.createElement('h3');
    h3.textContent = `${userInpU} gives you`;
    div.appendChild(h3);
     
    for (let i in morseTranslation) {
        let p = document.createElement('p');
        p.textContent = morseTranslation[i];
        div.appendChild(p)
    }
}
