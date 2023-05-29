let currentURL = window.location.search;

let url_params = new URLSearchParams(currentURL);
let firstname = url_params.get('firstname');
let lastname = url_params.get('lastname');

console.log(firstname);
console.log(lastname);

let body = document.body;
let p = document.createElement('p');
p.textContent = `${firstname}, ${lastname}`;
body.appendChild(p);
