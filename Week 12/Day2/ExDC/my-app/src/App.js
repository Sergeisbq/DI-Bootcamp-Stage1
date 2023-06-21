import logo from './logo.svg';
import './App.css';
import RobotContainer from './components/RobotContainer';
import React from 'react';
// import { connect } from 'react-redux';
import { searchRobot, getRobots } from './redux/actions'
import {useEffect} from 'react';
import {useDispatch} from 'react-redux';

const usersUrl = "https://jsonplaceholder.typicode.com/users";

const App = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    fetch(usersUrl)
      .then((res) => res.json())
      .then((users) => dispatch(getRobots(users)))
      .catch(console.error)
  }, [])

  //[] --> this function is going to be called when the component mounts
  //[value] --> this function is going to be called when value changes in the state

  const handleChange = (e) => {
    const searchStr = e.target.value;
    dispatch(searchRobot(searchStr)) // {type: "SEARCH_ROBOT", payload: searchStr}
    console.log('change');
  }

    return (
      <div className="tc">
        <h1 className="title">ROBOFRIENDS</h1>
        <div className="pa2">
          <input type="search" placeholder="search robots" className="pa3 ba b--green bg-lightest-blue" onChange={handleChange}/>
        </div>
        <RobotContainer/>
      </div>
    )
}

export default App;
