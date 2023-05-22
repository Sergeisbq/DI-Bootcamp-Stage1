
// let new_sel = document.getElementById("genres");
// let new_opt = document.createElement("option");
// new_opt.innerHTML = 'Classic';
// new_opt.value = 'classic';
// let old_sel = document.getElementById("genres").firstElementChild.nextElementSibling;
// old_sel.selected = false;
// new_opt.selected  = true;
// new_sel.appendChild(new_opt);


// let btn = document.getElementsByTagName("input");
// console.log(btn[0]);
// let sel = document.getElementById("colorSelect");
// btn[0].addEventListener("click", function() {
//     let to_rem = sel.options[colorSelect.selectedIndex];
//     sel.removeChild(to_rem);
// });


let shoppingList = [];

let div = document.getElementById("root");

let form = document.createElement("form");
let input_t = document.createElement("input");
input_t.type = "text";
form.appendChild(input_t);
let input_b = document.createElement("input");
input_b.type = "button";
input_b.value = "AddItem";
form.appendChild(input_b);
let input_b_c = document.createElement("input");
input_b_c.type = "button";
input_b_c.value = "ClearAll";
form.appendChild(input_b_c);

div.appendChild(form);

input_b.addEventListener('click', function(e) {
    shoppingList.push(input_t.value);
    console.log(shoppingList);
})

input_b_c.addEventListener('click', function(e) {
    shoppingList = [];
    console.log(shoppingList);

})


