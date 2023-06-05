// Here are the most commonly used HTTP verbs / actions
// GET: GET requests are only used to retrieve data.
// POST: POST requests are used to send new data.
// PUT: PUT requests are used to modify data.
// DELETE: DELETE requests deletes the specified data.
// PATCH: PATCH requests are used to partially modify data.DELETE

// CRUD routes conventions
// Create, Read, Update and Delete.

// Create: POST http://www.example.com/customers
// Read: GET http://www.example.com/customers/3814
// Update: PUT http://www.example.com/customers/3814
// Destroy: DELETE http://www.example.com/customers/3814

const express = require('express');
const {products} = require('./config/data.js');
const app = express();

// user request -> middelware -> response
const logger = (req, res, next) => {
    console.log('url=>', req.url);
    console.log('params=>', req.params);
    console.log('query=>', req.query);
    console.log('body=>', req.body);
    next()
}

const auth = (req, res, next) => {
    const user = req.query.user;
    if (user === 'admin') {
        next()
    }
    else {
        res.status(401).send('Unauthorized')
    }
}

// app.use('/api/pruducts', logger)
// app.use('/api/pruducts', auth)


app.use(express.urlencoded({extended:true}));
app.use(express.json())

// console.log(products);
app.listen(3001, () => {
    console.log('server is running on port 3001');
})


// http://localhost:3001/api/pruducts
// app.get('/api/pruducts', (req, res) => {
//     res.send('Hello')
// })


// GET - get all products
// CRUD - READ - GET
app.get('/api/pruducts', auth, (req, res) => {
    res.json(products)
})


// POST - to create a new product
// CRUD - CREATE - POST
app.post('/api/products', (req, res) => {
    products.push(req.body);
    res.send('ok from post')
})


// DELETE -
// CRUD - DESTROY/DELETE
app.delete('/api/pruducts/:product_id', (req, res) => {
    const id = req.params.product_id;
    const index = products.findIndex(item => item.id == id)
    if (index === -1) {
        return res.status(404).json({message: "Product not found"})
    }
    products.splice(index, 1);
    res.status(201).json(products)
})


// PUT - update a product
// CRUD - UPDATE - PUT
app.put('/api/products/:product_id', (req, res) => {
    const id = req.params.product_id;
    console.log('kkkkkkkkk');
    const index = products.findIndex(item => item.id == id)
    if (index === -1) {
        return res.status(404).json({message: "Product not found"})
    }
    products[index] = {
        ...products[index],
        name: req.body.name,
        price: req.body.price
    }
    return res.status(200).json(products)
})

// GET - get one of the product with the id
// CRUD - READ - get
// /api/products/132
app.get('/api/pruducts/:product_id', (req, res) => {
    const id = req.params.product_id;
    const product = products.find(item => item.id == id);
    if (!product) {
        return res.status(404).json({message: "Product not found"})
    }
    res.status(201).json(product)
})

//GET - search for a product by name 
// CRUD - READ - GET
// api/search
app.get('/api/search', (req, res) => {
    console.log(req.query);
    const product_name = req.query.name;
    const filtered = products.filter(item => {
        return item.name.toLowerCase().includes(product_name.toLowerCase())
    })
    if (filtered.length === 0) {
        return res.status(200).json({message: "No products matched your search"})
    }
    res.json(filtered)
    res.send('ok')
})