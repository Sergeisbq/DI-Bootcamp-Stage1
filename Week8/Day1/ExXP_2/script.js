//-----1.1-----
setTimeout(function(){
    alert('Hello World');
}, 1000*2);

//-----1.2-----
setTimeout(function(){
let div_1 = document.getElementById('container');
let p_new = document.createElement('p');
p_new.innerText = 'Hello World';
div_1.appendChild(p_new);

}, 1000*2);

//-----1.3-----
function clear_inter() {
    clearInterval(id)
}

let id = setInterval(function() {
    let div_1 = document.getElementById('container');
    let p_new = document.createElement('p');
    p_new.innerText = 'Hello World';
    div_1.appendChild(p_new);;
    if (div_1.children.length == 5) {
        clearInterval(id);
    }
}, 1000*2);

