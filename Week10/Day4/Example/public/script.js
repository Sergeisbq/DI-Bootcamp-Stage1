const getMyProducts = async () => {
    try {
        const res = await fetch('http://localhost:3030/api/products');
        const data = await res.json();
        console.log(data);
        render(data);
    }
    catch (e) {
        console.log(e);
    }
}

const render = (arr) => {
    const html = arr.map(item => {
        return `<div style="display:inline-block; border:1px solid black; margin:20px; padding:10px;">
        <h2>${item.name}</h2>
        <p>${item.price}</p>
        </div>`;
    })
    document.getElementById('root').innerHTML = html.join('')
}
getMyProducts()

