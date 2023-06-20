import { INSERT, UPDATE, DELETE, UPDATE_INDEX } from './actions';
import { addToLocalStorage, getFromLocalStorage } from '../utils/storage';

const initState = {
    list: getFromLocalStorage('transactions'),
    currentIndex: -1
}

export const reducer = (state=initState, action={}) => {
    switch (action.type) {
        case INSERT:
            state.list.push(action.payload)
            addToLocalStorage('transactions', [...state.list])
            return {...state, list: [...state.list], currentIndex: -1}
        case UPDATE:
            state.list[state.currentIndex] = action.payload
            addToLocalStorage('transactions', [...state.list])
            return {...state, list:[...state.list], currentIndex: -1}
        case UPDATE_INDEX:
            return {...state, currentIndex: action.payload}
        case DELETE:
            state.list.splice(action.payload, 1)
            addToLocalStorage('transactions', [...state.list])
            return {...state, list:[...state.list], currentIndex: -1}
        default:
            return {...state}
    }
}