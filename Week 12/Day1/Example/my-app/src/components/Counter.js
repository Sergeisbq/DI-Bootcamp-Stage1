import {useState} from 'react';
import {connect, useSelector, useDispatch} from 'react-redux';
import { incrementCounter, decrementCounter, incrementIfOdd } from '../redux/actions';

const Counter = (props) => {
    const count = useSelector((state) => state.count);
    const dispatch = useDispatch()
    const incrementOneSec = () => {
        setTimeout(() => {
          dispatch(incrementCounter());
        }, 1000);
      };
    return (
        <>
            <p>Clicked: {count} times</p>
            <button onClick={()=>dispatch(incrementCounter())}>+</button>
            <button onClick={()=>dispatch(decrementCounter())}>-</button>
            <button onClick={()=>dispatch(incrementIfOdd())}>Increment if odd</button>
            <button onClick={incrementOneSec}>Increment async</button>
        </>
    )
}

export default Counter






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