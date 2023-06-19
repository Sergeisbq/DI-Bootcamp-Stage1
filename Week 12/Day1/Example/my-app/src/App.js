// import logo from './logo.svg';
// import './App.css';
// import Test from './components/Test';
// import {useState} from 'react';


// function App() {
//   const [title, setTitle] = useState('My title');
//   return (
//     <div className="App">
//       <Test title={title} setTitle={setTitle}/>
//     </div>
//   );
// }

// export default App;

import logo from './logo.svg';
import './App.css';
import Test from './components/Test';
import React from 'react';
import {connect} from 'react-redux';
import {changePropOne} from './redux/actions';
import Counter from './components/Counter';



class App extends React.Component {
  constructor() {
    super();
    this.state = {
      property_one: 'text one',
    }
  }

  render() {
    return (
      <div className="App">
        {/* <h2>Simple Redux Example</h2>
        <div>
          Change prop One:<input onChange={this.props.changeOne}/>
        </div>
        <div>{this.state.property_one}</div>
        <div>{this.props.a}</div>
        <Test title='test'/> */}
        <Counter />
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  console.log(state);
  return {

  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    changeOne: (e) => dispatch(changePropOne(e.target.value))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App); // mapDispatchToProps

