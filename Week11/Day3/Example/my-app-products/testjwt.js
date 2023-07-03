const jwt = require('jsonwebtoken')

const token = jwt.sign(
    {name: 'John', email: 'lohn@gmail.com', id: 16},
    '@456$tgf7*',
    {
        expiers: '60s'
    },
)

console.log(token);

const oldtoken = ''

jwt.verify(oldtoken, '@456$tgf7*', (err, decoded) => {
    if (err) return console.log(err);
    console.log(decoded);
});