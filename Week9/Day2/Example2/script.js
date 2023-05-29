// function getX() {
//     setTimeout(() => {
//         return 5;
//     }, 1000)
    
// }

// function getY() {
//     return 6;
// }

// function getXY() {
//     let x = getX();
//     let y = getY();
//     console.log(x + y);
// }

// getXY()


///////!!!!!//////

// function getX(callback) {
//     console.log('Waiting for x...');
//     setTimeout(() => {
//         console.log('Getting x...');
//         callback(5);
//     }, 1000)
// }

// function getY(callback) {
//     console.log('Getting y...');
//     callback(6);
// }

// const getXY = () => {
//     getX((x) => {
//         getY((y) => {
//             console.log(x + y);
//         })
//     })
// }

// getXY()


// !!! Promise
// 1. Pending;
// 2. fullfield - resolve;
// 3. fullfield - reject;

// const p = new Promise((resolve, reject) => {
//     resolve('Promise was resolve')
// })

// console.log(p);


// // !!! //
// const flip = () => {
//     const coin = Math.floor(Math.random() * 3);
//     return (coin < 2) ? 
//            (coin == 0) ? 'head' : 'tail' : 'side';
// }

// // console.log(flip());

// const flipCoin = new Promise((resolve, reject) => {
//     const flipResult = flip();
//     if (flipResult == 'head' || flipResult == 'tail') {
//         resolve(flipResult);
//     }
//     else {
//         reject(flipResult);
//     }
// })

// console.log('flipping a coin...');
// // console.log(flipCoin);
// flipCoin
// .then((res) => {
//     console.log('resolve', res);
// })
// .catch((e) => {
//     console.log('reject', e);
// })



//////// !!!!!!
// const getX = () => {
//     return new Promise((res, rej) => {
//         setTimeout(() => {
//             res(5)
//         }, 2000)
//     })
// }

// const getY = () => {
//     return new Promise((res, rej) => {
//         setTimeout(() => {
//             res(6)
//         }, 2000)
//     })
// }

// const getXY = () => {
//     let x = getX();
//     // console.log('x =>', x);
//     x.then(x => {
//         // console.log(x);
//         let y = getY();
//         // console.log('y =>', y);
//         y.then(y => {
//         console.log(x + y);
//     })
//     })
//     .catch(e => {
//         console.log('reject', e);
//     })
// }

// console.log('before');
// getXY()
// console.log('after');



// const p = new Promise((res, rej) => {
//     // res('hello');
//     rej('hello');
// })

// p.then(res => {
//     // console.log(res);
//     return res + '#'
// })

// .then(res => {
//     // console.log(res);
//     return res + '@'
// })

// .then(res => {
//     console.log(res);
// })

// .catch(e => {
//     console.log('reject', e);
// })


// const testNum = new Promise((res, rej) => {
//     userNum = parseInt(prompt('Type a number'))
//     if (userNum < 10) {
//         res('number is less than 10, success!!!')
//     }
//     else {
//         rej('number is greater or equal to 10, error!!!')
//     }
//     // res('hello');
//     // rej('hello');
// })

// testNum.then(res => {
//     console.log(res);
// })

// .catch(rej => {
//     console.log(rej);
// })

//////===

// const testNum = num => {
//     return new Promise((res, rej) => {
//         if (num < 10) {
//             res(num + 'is less then 10')
//         }
//         else {
//             rej(num + 'is greater or equal to 10')
//         }
// })
// }

// testNum(5)
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log(err);
// })



// let res = fetch ('https://jsonplaceholder.typicode.com/users');
// console.log(res);

// let user = {
//     name: 'aaa',
//     username: 'aaaaaa'
// }
// fetch('https://jsonplaceholder.typicode.com/users/', {
//     method: 'POST',
//     headers: {
//         'Content-type': 'application/json'
//     },
//     body: JSON.stringify(user)
// })

// res.then(res => {
//     let json = res.json();
//     return json
// })
// .then(data => {
//     console.log(data);
// })

// console.log(res[0].address);



// const url = 'https://love-calculator.p.rapidapi.com/getPercentage?sname=Alice&fname=John';
// const options = {
// 	method: 'GET',
// 	headers: {
// 		'X-RapidAPI-Key': 'SIGN-UP-FOR-KEY',
// 		'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
// 	}
// };

// fetch(url, options)
// .then(res => res.json())
// .then(data => {
//     let root = document.getElementById('root');
//     root.innerHTML = `<div>
//     ${data.fname} ${data.sname} ${data.percentage} ${data.result}
//     </div>`
//     // console.log(data);
// })



//// Static function on promises

// Promise.all(...);
// Promise.allSettled(...);
// Promise.race(...);

// const promise1 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve('Resolve promise1')
//     }, 2000)
    
// })

// const promise2 = new Promise((resolve, reject) => {
//     reject('Resolve promise2')
// })

// const promise3 = new Promise((resolve, reject) => {
//     resolve('Resolve promise3')
// })

// Promise.all([promise1, promise2, promise3])
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log(err);
// })

// Promise.allSettled([promise1, promise2, promise3])
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log(err);
// })

// Promise.race([promise1, promise2, promise3])
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log(err);
// })


const urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/albums"
];

const arrPromises = urls.map( url => {
    return fetch(url).then(res => res.json())
})

// const proms = [];
// for (i in urls) {
//     proms.push(urls[i])
// }

// console.log(proms);
// for (item of proms) {
//     fetch(item).then(res => res.json())
// }
// const proms = [
//     fetch(urls[0]).then(res => res.json()),
//     fetch(urls[1]).then(res => res.json()),
//     fetch(urls[2]).then(res => res.json()),
// ]

Promise.all(arrPromises)
.then(res => {
    console.log(res);
})
.catch(err => {
    console.log(err);
})

// Promise.allSettled(urls)
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log(err);
// })

// Promise.race(urls)
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log(err);
// })

// fetch(url).then(res => res.json())