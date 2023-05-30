// -----1/2-----

let arr = [];
let div = document.getElementById('gifs');
let button = document.createElement('button');
button.textContent = 'Delete All';
button.addEventListener('click', deleteAll);
div.appendChild(button);

function handleSubmit(e) {

    e.preventDefault();
    let form1 = document.forms.myForm;
    let elems = form1.elements;
    let input = elems[0];
    q = input.value;
        
    let limit = 1;
    let offset = 0;
    let url = `https://api.giphy.com/v1/gifs/search?q=${q}&rating=g&offset=${offset}&limit=${limit}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`;

    gifAsync(url);
}

async function gifAsync(url) {
    const res = await fetch(url);
    const data = await res.json();
    arr.push(data) 

    let form1 = document.forms.myForm;
    let elems = form1.elements;
    let input = elems[0];
    q = input.value;

    let div = document.getElementById('gifs');
    let div2 = document.createElement('div');
    let img = document.createElement('img');
    let p = document.createElement('p');

    let button = document.createElement('button');
    button.textContent = 'Delete this gif';
    button.addEventListener('click', deleteGif);
    
    p.textContent = `Category - ${q}`;
    img.src = data.data[0].images.original.url;
    div.appendChild(div2);
    div2.appendChild(img);
    div2.appendChild(p);
    div2.appendChild(button);

    console.log(arr);

}

function deleteAll(event) {
    const gifsToDel = event.target.parentNode;
    gifsToDel.remove();
}

function deleteGif(event) {
    const gifToDel = event.target.parentNode;
    gifToDel.remove();
}
