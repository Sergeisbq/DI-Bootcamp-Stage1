


// let id_c;
// console.log(`${id_c} 'hello'`);

// function handleClick(e) {
//     console.log(e.target, e.type);
//     XMLDocument()
// }

// function handleInput(e) {
//     console.log(e.target.value);
//     console.log(e.target.name);
// }


// function handleDivClick(e) {
//     let div = e.target;
//     console.log(div.children);
// }

// let root = document.getElementById('root');

// let butB = document.createElement('button');

// butB.innerText = 'Click Me B!';
// root.appendChild(butB);

// butB.addEventListener('click', function(e) {
//     console.log(e.target, 'tjghjrkt');
// })

// let butA = document.getElementById('buta');
// butA.addEventListener('click', function(e) {
//     console.log('Button A');
// })


// function insertRow() {
//     let table = document.getElementById("sampleTable");
//     let tr = document.createElement('tr');
//     table.firstElementChild.appendChild(tr);
//     let td = document.createElement('td');
//     let rows = document.getElementsByTagName('tr');
//     td.innerText = `Row${rows.length} cell1`;
//     tr.appendChild(td);
//     let td1 = document.createElement('td');
//     td1.innerText = `Row${rows.length} cell2`;
//     tr.appendChild(td1);

// }


// function insertRow2() {
//     let table = document.getElementById('sampleTable').firstElementChild;
//     // let row = document.createElement('tr');
//     let row = table.firstElementChild;
//     const rownum = table.children.length;
//     const newRow = row.cloneNode(true);
//     newRow.firstElementChild.innerText = `Row${rownum+1} cell1`;
//     newRow.lastElementChild.innerText = `Row${rownum+1} cell2`;

//     table.appendChild(newRow);
// }


// const div1 = document.getElementById('div1');

// const div2 = document.getElementById('div2');

// const but = document.getElementById('but');

// div1.addEventListener('click', function(e) {
//     alert('DIV 1!');
// })

// div2.addEventListener('click', function(e) {
//     alert('DIV 2!');
// })

// but.addEventListener('click', function(e) {
//     alert('BUT!');
//     e.stopPropagation();
// })



// // console.log(document.forms.form_one);
// const frm = document.forms.form_one;
// const elems = frm.elements;
// console.log(elems);

// // function handleSubmit(e) {
// //     e.preventDefault();
// //     let val = elems.username.value;
// //     val = val.replaceAll(' ', '');
// //     val = val.trim();
// //     let psw = elems.password.value;
// //     if (val.length > 0 && psw.length >= 6) {
// //         console.log(val);
// //         console.log(psw);
// //     }

//     // console.log(val);
//     // console.log(psw);

// //     e.target.submit();
// // }


// frm.elements.fruits.selectIndex = 1



// function handleSubmit(e) {
//     e.preventDefault();
//     const fruit = frm.elements.fruits.value;
//     console.log(fruit.trim());
// }





// function x() {
//     console.log('hello');
// }


// // setTimeout(function(){
// //     x();
// // }, 1000*3);

// // setTimeout(x, 1000*3);

// // let counter = 0;
// // let id = setInterval(function() {
// //     counter++
// //     console.log(counter);
// //     if (counter > 5) {
// //         clearInterval(id);
// //     }
// // }, 1000*5);

// // let id_c;


// function y() {

//     let pos = 0;
//     let cube = document.getElementById("inner");
//     id_c = setInterval( function() {
//         if (pos >= 350) {
//             clearInterval(id_c);
//         }
//         pos++;
//         cube.style.left = pos+"px";
//         }, 5)
// }

// function z() {
//     clearInterval(id_c);
// }
// setTimeout(y, 1000*6);