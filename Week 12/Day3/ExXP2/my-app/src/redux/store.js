import {createStore, applyMiddleware} from 'redux';
import {reducer} from './reducer';
// import thunk from 'redux-thunk'

// => action => middleware => reducer

const logger = (store) => (next) => (action) => {
    console.log('state', store.getState());
    next(action)
    console.log('caught in the middleware', store.getState());
}

const store = createStore(reducer, applyMiddleware(logger));

export default store;