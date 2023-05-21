// //-----1-----
// let h1 = document.getElementsByTagName('h1');
// console.log(h1);

// let article = document.getElementsByTagName('article');
// console.log(article[0].firstElementChild);
// article[0].removeChild(article[0].lastElementChild);

// let h2 = document.getElementsByTagName('h2');
// h2[0].addEventListener('click', function(e) {
//     h2[0].style.background = 'red';
// })

// let h3 = document.getElementsByTagName('h3');
// h3[0].addEventListener('click', function(e) {
//     h3[0].style.display = 'none';
// })

// let body = document.body;
// let but_B = document.createElement('button');
// but_B.innerText = 'Make it Bold';
// body.appendChild(but_B);
// but_B.addEventListener('click', function(e) {
//     body.style.fontWeight = 'bold';
// })



// // -----2-----
// console.log(document.forms[0]);
// console.log(document.getElementsByTagName('input'));
// let input = document.getElementsByTagName('input');
// for (let item of input) {
//     if (item.name) {
//         console.log(item.name);
//     }
// }

// function handleSubmit(e) {
//     e.preventDefault();
//     let fn = input.fname.value;
//     fn = fn.replaceAll(' ', '');
//     fn = fn.trim();
//     let ln = input.lname.value;
//     ln = ln.replaceAll(' ', '');
//     ln = ln.trim();
//     if (fn.length > 0 && ln.length > 0) {
//         let ul = document.getElementsByClassName("usersAnswer");
//         let lif = document.createElement('li');
//         lif.innerText = `${fn}`;
//         ul[0].appendChild(lif);
//         let lil = document.createElement('li');
//         lil.innerText = `${ln}`;
//         ul[0].appendChild(lil);
//     }
// }


//-----3-----
let allBoldItems = [];
function getBold_items() {
    for (let item of document.getElementsByTagName('strong')) {
        allBoldItems.push(item);
    }
}
getBold_items()
console.log(allBoldItems);

function highlight() {
    for (let item of allBoldItems) {
        item.style.color = "blue";
    }
}

function return_normal() {
    for (let item of allBoldItems) {
        item.style.color = "black";
    }
}

let p = document.getElementsByTagName("p");
console.log(p[4]);
p[4].addEventListener("mouseover", mouseOver);
p[4].addEventListener("mouseout", mouseOut);

function mouseOver() {
    highlight();
}

function mouseOut() {
    return_normal();
}
