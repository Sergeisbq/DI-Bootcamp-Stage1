const bcrypt = require('bcrypt');
const axios = require('axios');
const slugify = require('slugify');



const salt = bcrypt.genSaltSync(10);

const hash = bcrypt.hashSync('123456', salt);

console.log(hash);

console.log(slugify('my new website'));

// axios.get('https://jsonplaceholder.typicode.com/users')
//   .then(res => {
//     // handle success
//     console.log(res.data);
//   })
//   .catch((e) => {
//     // handle error
//     console.log(e);
//   })


