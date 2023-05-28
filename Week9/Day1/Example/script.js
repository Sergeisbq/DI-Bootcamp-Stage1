
let form1 = document.forms.myForm

let elems = form1.elements;

let select = elems[2]

function handleSubmit(e) {
    e.preventDefault();
    // console.log("Hi");
    let selected = Array.from(select.options)
    .filter(option => option.selected)
    .map(option => option.value)
    console.log(selected);

}