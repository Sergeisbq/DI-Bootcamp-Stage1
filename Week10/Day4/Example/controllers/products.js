const {
    getAllProducts,
    getProduct,
    searchProduct,
    createProduct,
    deleteProduct,
    updateProduct
} = require('../modules/products.js');

// READ - GET all products

const _getAllProducts = (req, res) => {
    getAllProducts()
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({msg:err.message})
    })
}

const _getProduct = (req, res) => {
    const id = req.params.id;
    getProduct(id)
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({msg:err.message})
    })
}

const _searchProduct = (req, res) => {
    searchProduct(req.query.name)
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({msg:err.message})
    })
}

const _createProduct = (req, res) => {
    createProduct(req.body)
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({msg:err.message})
    })
}

const _deleteProduct = (req, res) => {
    const id = req.params.id;
    deleteProduct(id)
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({msg:err.message})
    })
}

const _updateProduct = (req, res) => {
    const id = req.params.id;
    const product = req.body;
    updateProduct(id, product)
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({msg:err.message})
    })
}

module.exports = {
    _getAllProducts,
    _getProduct,
    _searchProduct,
    _createProduct,
    _deleteProduct,
    _updateProduct
}