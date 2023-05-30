// -----1/2-----
// let q = 'sun';
// let limit = 10;
// let offset = 2;
// let url = `https://api.giphy.com/v1/gifs/search?q=${q}&rating=g&offset=${offset}&limit=${10}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`;

// async function gifAsync() {
//     const res = await fetch(url);
//     const data = await res.json();
//     console.log(data);
// }

// gifAsync()


// // -----3-----
// async function gifAsync2() {

//     try{
//         const res = await fetch("https://www.swapi.tech/api/starships/9/");
//         const data = await res.json();
//         console.log(data);
//     }

//     catch(err) {
//         console.log(err);
//         }
// } 

// gifAsync2()


// // -----4-----
// function resolveAfter2Seconds() {
//     return new Promise(resolve => {
//         setTimeout(() => {
//             resolve('resolved');
//         }, 2000);
//     });
// }

// async function asyncCall() {
//     console.log('calling');
//     let result = await resolveAfter2Seconds();
//     console.log(result);
// }

// asyncCall(); // first - 'calling', after 2 seconds - 'resolved'
