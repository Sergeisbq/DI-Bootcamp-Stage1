
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



console.log('before');

function x() {
    try {
        a;
    }
    catch (error) {
        // console.log('Something get wrong in x function line 5', error.message);
        // console.log(error.name);
        // console.log(error.stack);
        throw new Error('error in x function');
    }
}

try {
x()
}
catch (e) {
    console.log(e);
};
console.log('after');