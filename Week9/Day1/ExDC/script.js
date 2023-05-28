//-----1-----

let form1 = document.forms.myForm
let elems = form1.elements;

function handleSubmit(e) {
  e.preventDefault();
  let firstName = elems.firstname.value;
  let lastName = elems.lastname.value;
  let proFile = {
    name : firstName,
    lastname : lastName,
  }
  let myJSON = JSON.stringify(proFile);
  let body = document.body;
  let p = document.createElement('p');
  p.textContent = myJSON;
  body.appendChild(p);
}
