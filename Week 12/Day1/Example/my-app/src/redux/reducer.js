const initState = {
    property_one: 'Hello from store',
    property_two: 'bla bla bla',
    count: 0
}

export const reducer = (state = initState, action={}) => {
    switch (action.type) {
        case 'PROP_ONE':
            return {...state, property_one:action.payload}
        
        case 'INCREMENT_COUNT':
            return {...state, count: state.count + 1}
        case 'DECREMENT_COUNT':
            return {...state, count: state.count - 1}

        default:
            return {...state}
    }
}