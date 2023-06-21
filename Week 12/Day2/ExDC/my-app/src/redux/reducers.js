const initialState = {
    users:[],
    inputValue : "",
};

export const reducer = (state = initialState, action={}) => {

    if (action.type === "SEARCH_ROBOT") {
        return {...state, inputValue:action.payload};
    } 

    else if (action.type === "GET_ROBOTS") {
        console.log("in reducer getrobots", action.payload);
        return {users : action.payload}
    }
    return state
}
