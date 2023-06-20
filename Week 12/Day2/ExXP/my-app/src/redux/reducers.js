const initState = {
    list: [],
    currentIndex: null
}


export const reducer = (state=initState, action={}) => {
    if (action.type === "INSERT") {
        console.log("REDUCER!!!!!!!!!!!!!!!!", action);
        const newList = [...state.list]; //copy of the list
        newList.push(action.payload); //push the new transaction
        return {...state, list:newList} //return the new state
    }
    else if (action.type === "DELETE") {
        const newList = [...state.list]; //copy of the list
        newList.splice(action.payload, 1); //del the transaction
        return {...state, list:newList} //return the new state
    }
    else if (action.type === "UPDATE") {
        const newList = [...state.list]; //copy of the list
        newList[state.list] = action.payload; //update the transaction
        return {...state, list:newList} //return the new state
    }
    return {...state}
}
