const {db} = require('../config/db.js');

const getAllProducts = () => {
    return db('products')
    .select('id', 'name', 'price')
    .orderBy('name')
}

const getProduct = (product_id) => {
    return db('products')
    .select('id', 'name', 'price')
    .where({id:product_id})
}

const searchProduct = (name) => {
    return db('products')
    .select('id', 'name', 'price')
    .whereILike('name', `${name}%`)
}

const createProduct = (product) => {
    return db('products')
    .insert(product) // {name: 'name', price: 900}
    .returning('*')
}

const deleteProduct = (product_id) => {
    return db('products')
    .where({id:product_id})
    .del()
    .returning('*')
}

const updateProduct = (product_id, product) => {
    return db('products')
    .update(product)
    .where({id:product_id})
    .returning('*')
}

module.exports = {
    getAllProducts,
    getProduct,
    searchProduct,
    createProduct,
    deleteProduct,
    updateProduct
}