const frm = document.getElementById("MyForm");
const elems = frm.elements;
console.log(elems);

function handleSubmit(e) {
    e.preventDefault();
    let radius = elems.radius.value;
    let volume = 3.14 * (parseInt(radius))**2;
    elems.volume.value = volume;
}

let p = document.getElementsByTagName('p');
p[0].addEventListener('click', function(e) {
    p[0].style.background = 'grey';
})

p[0].addEventListener('dblclick', function(e) {
    p[0].style.textAlign = 'end';
})

p[0].addEventListener('mouseover', function(e) {
    p[0].style.fontSize = '30px';
    p[0].style.background = 'pink';
})

p[0].addEventListener('mouseout', function(e) {
    p[0].style.fontSize = '15px';
    p[0].style.background = 'white';
})