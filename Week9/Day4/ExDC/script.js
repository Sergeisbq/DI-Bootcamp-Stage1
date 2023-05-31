let div = document.getElementById('frame');

let form = document.createElement('form');
form.setAttribute('id','myForm');
div.appendChild(form);

let selectFirst = document.createElement('select');
selectFirst.setAttribute('id','selF');
form.appendChild(selectFirst);

let selectSecond = document.createElement('select');
selectSecond.setAttribute('id','selS');
form.appendChild(selectSecond);


async function gifAsync() {

    let url = `https://v6.exchangerate-api.com/v6/4b0fa0de29dd640f37152e29/latest/USD`;
    const res = await fetch(url);
    const data = await res.json();
    let currKey = Object.keys(data.conversion_rates);
    let currVal = Object.values(data.conversion_rates);
    console.log(currKey); 
    console.log(currVal); 
    for (i in currKey) {
        console.log(currVal[i]); 
        let option1 = document.createElement('option');
        let option2 = document.createElement('option');
        option1.value = currVal[i];
        option1.textContent = currKey[i];
        option2.value = currVal[i];
        option2.textContent = currKey[i];
        selectFirst.appendChild(option1);
        selectSecond.appendChild(option2);
    }

    let inputGet = document.createElement('input');
    inputGet.placeholder = "Type the amount";
    inputGet.style.textAlign = "center";
    let inputOut = document.createElement('input');
    inputOut.placeholder = "Result";
    inputOut.style.textAlign = "center";
    let button1 = document.createElement('button');
    button1.setAttribute('class','toFindBtn');
    button1.addEventListener('click', calcCur);
    button1.textContent = "Convert";
    let button2 = document.createElement('button');
    button2.setAttribute('class','toFindBtn');
    button2.addEventListener('click', toSwitch);
    button2.textContent = "Replace";
    div.appendChild(inputGet);
    div.appendChild(inputOut);
    div.appendChild(button1);
    div.appendChild(button2);

}

gifAsync()

function calcCur() {
    let option11 = document.getElementById("selF").value;
    console.log(option11);
    let option22 = document.getElementById("selS").value;
    console.log(option22);
    let amount = document.getElementsByTagName("input")[0].value;
    console.log(amount);
    let result = document.getElementsByTagName("input")[1];
    result.value = parseInt(amount)/option11 * option22;
}


function toSwitch(e) {
    e.preventDefault();
    // let form = document.getElementById("myForm");
    let option11 = document.getElementById("selF");
    console.log(option11);
    let option22 = document.getElementById("selS");
    console.log(option22);
    let temp = option22.value;
    option22.value = option11.value;
    option11.value = temp;
}



let chars = ['A', 'B', 'A', 'C', 'B'];

let out = [];

for (let i = 0; i < chars.length; i++ ) {
    const element = chars[i];
    if (!out.includes(element)) {
        out.push(element);
    }
}

console.log(out);


let str = 'hello world';
let str2 = str.split('');
let str3 = str2.reverse();
let str4 = str3.join('');
console.log(str4);




