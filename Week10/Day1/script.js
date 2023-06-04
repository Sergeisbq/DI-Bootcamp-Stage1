const {carParam} = require('./cars.js')
const {usersInfo} = require('./users.js')


usersInfo()
.then(data => {
    console.log(data);
})
