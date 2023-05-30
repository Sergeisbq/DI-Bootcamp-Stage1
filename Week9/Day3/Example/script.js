// Async / Await

// function simpleAsync() {
//     return new Promise((res, rej) => {
//         res('1');
//     })
// }

// async function simpleAsync2() {
//     return '1'
// }

// simpleAsync()
// .then(res => {
//     console.log(res)
// })

// simpleAsync2()
// .then(res => {
//     console.log(res);
// })


// function returnPromise() {
//     return new Promise((res, rej) => {
//         setTimeout(() => {
//             console.log('Promise executed...');
//             res('sample data')
//         }, 3000)
//     })
// }

// async function exe() {
//     let name = 'John';
//     let p = await returnPromise();
//     console.log(p);
//     console.log(name);
// }

// exe()



// function returnPromise() {
//     return new Promise((res, rej) => {
//         setTimeout(() => {
//             console.log('Promise executed...');
//             rej('sample data')
//         }, 3000)
//     })
// }

// async function exe() {
//     let name = 'John';
//     try {
//         let p = await returnPromise();
//         console.log(p);
//     }

//     catch(e) {
//         console.log('hahaha');
//     }
    
//     console.log(name);
// }

// exe()




// function users() {
//     fetch('https://jsonplaceholder.typicode.com/users')
//     .then(res => {
//         res.json()
//     })
//     .then(data => {
//         console.log(data);
//     })
// }

// async function userAsync() {
//     const res = await fetch('https://jsonplaceholder.typicode.com/users');
//     const data = await res.json();
//     console.log(data);
// }

// userAsync()


// async function x() {

// }

// const y = async function() {

// }

// const a = async () => {

// }


// const timeout = async(milliseconds, id) => {
//     await new Promise((resolve, reject) => {
//         setTimeout(() => {
//             console.log(id, 'Done!');
//             resolve()
//         }, milliseconds)
//     })
// }

// async function x() {
//     console.log('before');

//     // ['first', 'second', 'third'].forEach(async (item) => {
//     //     await timeout(2000, item)
//     // }); ///!!!! Don not use if await for something

//     for (item of ['first', 'second', 'third']) {
//         await timeout(2000, item);
//     }
//     console.log('after');
// }

// x();



// const promise1 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve('promise1')
//     }, 2000)
// })

// const promise2 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve('promise2')
//     }, 2000)
// })

// const promise3 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve('promise3')
//     }, 2000)
// })


// Promise.all([promise1, promise2, promise3])
// .then(result => {
//     console.log(result);
// })
// .catch(err => {
//     console.log(err);
// })


// const data = async() => {
//     try {
//         const result = await Promise.all([promise1, promise2, promise3]);
//         console.log(result);
//     }
//     catch(err) {
//         console.log(err);
//     }
// }

// data()

let fibArr = [];
function fib(num) {

    fibArr = [0, 1];

    for (let i = 2; fibArr[i - 1] + fibArr[i - 2] <= num; i++) {
        fibArr.push(fibArr[i - 1] + fibArr[i - 2]);
        
    }
    console.log(fibArr); 
}


fib(200)
 

function fibSum(arr) {
    let j = 0;
    arr.forEach(item => {
        j += item
    });
    console.log(j);
}

fibSum(fibArr)
