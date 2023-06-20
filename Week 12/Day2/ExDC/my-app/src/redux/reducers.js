import { combineReducers } from "redux";

const initialState = [];

function robotReducer(state = initialState, action) {
    return state

}

export const rootReducer = combineReducers({
    robotReducer: robotReducer
})