export const changePropOne = (value) => {
    return {
        type: 'PROP_ONE',
        payload: value
    }
} 

export const changePropTwo = (value) => {
    return {
        type: 'PROP_TWO'
    }
} 



export const incrementCounter = () => ({
  type: 'INCREMENT_COUNT',
});

export const decrementCounter = () => ({
  type: 'DECREMENT_COUNT',
});