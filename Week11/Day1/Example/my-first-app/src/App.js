import logo from './logo.svg';
import './App.css';
import Hello from './Hello';
import User from './components/User';
import robots from './users.json';
import Robots from './components/Robots';
import RobotClass from './components/RobotClass';

console.log(robots);

function App() {

  const users = [
    {id: 1, name: 'aaa', email: 'aaa@gmail.com'},
    {id: 2, name: 'bbb', email: 'bbb@gmail.com'},
    {id: 3, name: 'ccc', email: 'ccc@gmail.com'},
    {id: 4, name: 'ddd', email: 'ddd@gmail.com'}
  ]
  return (
    <div className="App">
      <header className="App-header">
        {
          robots.map((item, i) => {
            return <RobotClass userinfo={item} key={i}/>
          })
        }

        {/* {
          robots.map((item, i) => {
            return <Robots userinfo={item} key={i}/>
          })
        } */}

        {/* {
          users.map(item => {
            return <User key={item.id} name={item.name} email={item.email} />
          })
        } */}

        {/* <User name="John" email="john@gmail.com" />
        <User name="Mary" email="mary@gmail.com" /> */}
        {/* <Hello /> */}
        
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
