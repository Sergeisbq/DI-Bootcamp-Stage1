//-----1-----

function makeAllCaps(arr) {
    return new Promise((res, rej) => {
        let arr2 = [];
        if (arr.length > 4) {
            let result = arr.every(function checkIsNum(item, index, arr) {
                if (typeof item === 'string') {
                    return true
                }
                else {
                    return false
                }
            }); 
            if (result == true) {
                arr.forEach(item => {
                    arr2.push(item.toUpperCase());
                    return res(arr2.sort());
                });
            }
            else {
                rej('There is a problem with items');
            }
        }
            
        else {
            rej('There is a problem with length');
        }
    });
}

arr1 = ["apple", "orange", "cherry", "watermelon", "banana"];
makeAllCaps(arr1)
.then(res => {
    console.log(res);
})
.catch(err => {
    console.log(err);
})
