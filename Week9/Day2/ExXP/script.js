//-----1-----

// const testNum = new Promise((res, rej) => {
//     userNum = parseInt(prompt('Type a number'))
//     if (userNum < 10) {
//         res('number is less than 10, success!!!')
//     }
//     else {
//         rej('number is greater or equal to 10, error!!!')
//     }
// })

// testNum
// .then(res => {
//     console.log(res);
// })
// .catch(rej => {
//     console.log(rej);
// })

////===

const testNum = num => {
    return new Promise((res, rej) => {
        if (num < 10) {
            res(num + ' is less then 10')
        }
        else {
            rej(num + ' is greater or equal to 10')
        }
})
}

testNum(15)
.then(res => {
    console.log(res);
})
.catch(err => {
    console.log(err);
})

testNum(8)
.then(res => {
    console.log(res);
})
.catch(err => {
    console.log(err);
})


//-----2-----

// const p = () => {
//     return new Promise((res, rej) => {
//         setTimeout(() => {
//             res('Success!')
//         }, 4000)
//     })
// }

// p()
// .then(res => {
//     console.log(res);
// })
// .catch(err => {
//     console.log('Ooops something went wrong');
// })


//-----3-----

// const j = () => {
//     return new Promise((res, rej) => {
//         res(3);
// })
// }

// const k = () => {
//     return new Promise((res, rej) => {
//         rej('Boo!');
// })
// }

// j()
// .then(res => {
//     console.log(res);
// })  

// k()
// .catch(err => {
//     console.log(err);
// })


