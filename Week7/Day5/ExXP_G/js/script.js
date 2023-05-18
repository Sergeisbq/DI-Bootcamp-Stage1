
let fl_param = '';

// function number(param) {
//     let div = document.getElementById("display");
//     fl_param += param.toString();
//     div.innerText = fl_param;

// }

// function operator() {

// }

// function equal() {

// }



let entr_n1 = '';
let entr_n2 = '';
let operation = '';
let curent_enter = '';

function number(ll){
  let div = document.getElementById('display');
  curent_enter+=ll.toString();
  div.innerText = curent_enter;
  console.log(curent_enter);
}

function operator(op){
  let res = 0
  if (op != '='){
    if (operation === ''){
      operation = op;
      entr_n1 = (entr_n1 === '') ? curent_enter: entr_n1;
      curent_enter = '';
    } else {
      entr_n2 = curent_enter;
      curent_enter = '';
      res = calculate();
      display_text(res)
      console.log(res);
    }
  } else {
    entr_n2 = curent_enter;
    curent_enter = '';
    res = calculate();
    display_text(res)
    console.log(res);
  }
}

//
function calculate(){
  let res = 0;
  switch (operation){
    case '+':
      res = parseFloat(entr_n1) + parseFloat(entr_n2);
      console.log('+', entr_n1, entr_n2, res);
      break;
    case '-':
      res = parseFloat(entr_n1) - parseFloat(entr_n2);
      break;
    case '*':
      res = parseFloat(entr_n1) * parseFloat(entr_n2);
      break;
    case '/':
      res = (parseFloat(entr_n2) !=0) ? (parseFloat(entr_n1) / parseFloat(entr_n2)) : 0;
      break;
  }
  entr_n1 = res.toString();
  return res;
}
function display_text(res){
  let div = document.getElementById('display');
  div.innerText = res.toString();
}


function clear_all(){
    let div = document.getElementById("display");
    div.innerText = 0;
    curent_enter = '';
  }

  function reset_all(){
    let div = document.getElementById("display");
    div.innerText = 0;
    entr_n1 = '';
    entr_n2 = '';
    operation = '';
    curent_enter = '';
  }












