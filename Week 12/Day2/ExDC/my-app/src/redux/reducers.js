const initialState = {
    users:[],
    inputValue : "",
    loading: true
};

export const reducer = (state = initialState, action={}) => {

    if (action.type === "SEARCH_ROBOT") {
        return {...state, inputValue:action.payload};
    } 

    else if (action.type === "GET_ROBOTS") {
        console.log("In GET", state.loading);
        console.log("in reducer getrobots", action.payload);
        return {users : action.payload}
    } 
    else if (action.type === "DONE_ROBOTS") {
        console.log("Before DONE", state.loading);
        console.log("in reducer DONE_ROBOTS");
        return {...state, loading : false}
    }
    return state
}
