// const getUsers = async (url) => {
//     const users = await fetch(url);
//     const res = users.json();
//     // const result = res.
//     return res[0]
// }

// module.exports = {
//     getUsers
// }


const usersInfo = async() => {
    try {
        const res = await fetch('https://jsonplaceholder.typicode.com/users');
        const users = res.json();
        return users
    }
    catch(e) {
        console.log(e);
    }
}


module.exports = {
    usersInfo
}