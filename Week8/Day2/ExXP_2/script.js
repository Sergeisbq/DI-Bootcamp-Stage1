
// //-----1-----
// const addition_1 = (a, b) => a + b


// //-----2-----
// const convert_1 = (a) => a * 1000; 


// //-----3-----
// const sif = (children, partners_name, location, job_title) => {
//     let body = document.body;
//     let p = document.createElement("p");
//     p.textContent = `"You will be a ${job_title} in ${location}, and married to ${partners_name} with ${children} kids."`;
//     body.appendChild(p);
// }
// sif(2, 'Sasha', 'TA', "CEO")


// //-----4-----
// const sif = (name) => {
//     let nb = document.getElementById("nb");
//     let div = document.createElement("div");
//     div.textContent = `${name}`;
//     let img = document.createElement("img");
//     img.src = "https://i.guim.co.uk/img/media/b0946a2bbaaa289e8a3326ccde9362f01b42bce3/0_55_1642_986/master/1642.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=0ec4193b9a33af563ca7b28534254ef8";
//     img.width = "30";
//     img.height = "30";
//     nb.appendChild(div);
//     div.appendChild(img);
// }

// sif("John");


// //-----5-----
const makeJuice = (size) => {
    let ingr = []
    const addIngredients = (ing_1, ing_2, ing_3) => {
        ingr.push(ing_1);
        ingr.push(ing_2);
        ingr.push(ing_3);
        // let body = document.body;
        // let p = document.createElement('p');
        // p.textContent = `The client wants a ${size} juice, containing ${ing_1}, ${ing_2}, ${ing_3}"`;
        // body.appendChild(p);
    }
    addIngredients('apple', 'orange', 'banana');
    addIngredients('cherry', 'coconut', 'pineapple');
    // console.log(ingr);
    const displayJuice = () => {
        let body = document.body;
        let p = document.createElement('p');
        p.textContent = `The client wants a ${size} juice, containing ${ingr[0]}, ${ingr[1]}, ${ingr[2]}, ${ingr[3]}, ${ingr[4]}, ${ingr[5]}"`;
        body.appendChild(p);
    }
    displayJuice();
}
makeJuice('Medium');


