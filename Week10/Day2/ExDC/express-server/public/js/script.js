let form = document.getElementById('myForm');

function getData(e) {
    e.preventDefault();
    let elems = form.elements;
    const email = elems.email.value;
    const mes = elems.message.value;
    const body = {
    email: email,
    message: mes
    };

    fetch("/formData", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    })
        .then((res) => res.text())
        .then((res) => displayResponse(res))
        .catch((e) => console.error(e))
}

form.addEventListener('submit', getData);




// function displayResponse(text) {
//     const body = document.body;
//     const p = document.createElement('p');
//     p.textContent = text;
//     body.appendChild.p
// }


function displayResponse(response) {
    const p = document.getElementById("res");
    p.textContent = response;
  }






