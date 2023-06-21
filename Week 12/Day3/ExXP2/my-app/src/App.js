import logo from './logo.svg';
import './App.css';
import {useState} from 'react';
import {connect, useSelector, useDispatch} from 'react-redux';
import { incrementCounter, decrementCounter } from './redux/actions';



function App() {
  const count = useSelector((state) => state.age);
  const dispatch = useDispatch()
  return (
    <>
        <p>Redux Middleware Counter Action:</p>
        <p>your age: {count}</p>
        <button onClick={()=>dispatch(incrementCounter())}>Age UP</button>
        <button onClick={()=>dispatch(decrementCounter())}>Age DOWN</button>
    </>
)
}

export default App;




