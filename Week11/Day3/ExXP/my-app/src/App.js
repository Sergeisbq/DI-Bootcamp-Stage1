import logo from './logo.svg';
import './App.css';
import React from 'react';

// import BuggyCounter from './components/BuggyCounter';
// import ErrorBoundary from './components/ErrorBoundary';
// import Colors from './components/Colors';
// import Child from './components/Child';

class Child extends React.Component {

  componentWillUnmount() {
    alert('Component named Header is about to be unmounted!')
  }

  render() {
      return (
          <div>
              <h1>Hello World!</h1>
          </div>
      )
  }
}


class App extends React.Component {
  constructor() {
    super();
    this.state = {
        show: true,
    };
  }

  toDel = () => {
      this.setState({show: false});
      // console.log(this.state.show);
  }

  render() {
      return (
          <div>
              { this.state.show && <Child /> }
              <button onClick={this.toDel}>Delete Header</button>
          </div>
      )
  }

}

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">

//         {/* <ErrorBoundary>
//           <BuggyCounter />
//         </ErrorBoundary>

//         <ErrorBoundary>
//           <BuggyCounter />
//         </ErrorBoundary>

//         <BuggyCounter /> */}

//         {/* <Colors /> */}

//       </header>
//     </div>
//   );
// }

export default App;
