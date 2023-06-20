const initState = {
    count: 0
}

export const reducer = (state = initState, action={}) => {
    switch (action.type) {
        case 'INCREMENT_COUNT':
            return {...state, count: state.count + 1}
        case 'DECREMENT_COUNT':
            return {...state, count: state.count - 1}
        case 'INCREMENT_IF_ODD':
            if (state.count % 2 !== 0) {
                return {...state, count: state.count + 1}
            }
        default:
            return {...state}
    }
}