let url = 'http://localhost:3000/';

async function gifAsync() {
    const res = await fetch(url);
    console.log(res);
    const data = await res.json();
    console.log("data", data);
}

gifAsync()

const funcAlert = () => {
    alert('Hello from JavaScript');
}

console.log("test");

let btn = document.getElementById('btn');
btn.addEventListener('click', funcAlert);

