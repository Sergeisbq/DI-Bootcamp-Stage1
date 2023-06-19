import {useState} from 'react';
import {connect, useSelector, useDispatch} from 'react-redux';
import { incrementCounter, decrementCounter } from '../redux/actions';

const Counter = (props) => {
    // const [count, setCount] = useState(0)
    const count = useSelector((state) => state.count);
    const dispatch = useDispatch()
    // return (
    //     <>
    //         <button onClick={()=>props.handleIncrement()}>+</button>
    //         {props.count}
    //         <button onClick={()=>props.handleDecrement()}>-</button>
    //     </>
    // )
    return (
        <>
            <button onClick={()=>dispatch(incrementCounter())}>+</button>
            {count}
            <button onClick={()=>dispatch(decrementCounter())}>-</button>
        </>
    )
}

// const mapStateToProps = (state) => {
//     return {
//         count: state.count
//     }
// }

// const mapDispatchToProps = (dispatch) => {
//     return {
//         handleIncrement: () => dispatch(incrementCounter()),
//         handleDecrement: () => dispatch(decrementCounter()),
//     }
// }

// export default connect(mapStateToProps, mapDispatchToProps)(Counter)
export default Counter





// import React from 'react';
// import { connect } from 'react-redux';
// import { incrementCount, decrementCount } from '../redux/actions';

// const Counter = (props) => {
//   const { count, increment, decrement } = props;

//   return (
//     <>
//       <button onClick={increment}>+</button>
//       {count}
//       <button onClick={decrement}>-</button>
//     </>
//   );
// };

// const mapStateToProps = (state) => ({
//   count: state.count,
// });

// const mapDispatchToProps = (dispatch) => ({
//   increment: () => dispatch(incrementCount()),
//   decrement: () => dispatch(decrementCount()),
// });

// export default connect(mapStateToProps, mapDispatchToProps)(Counter);