import logo from './logo.svg';
import './App.css';
import Test from './components/Test';
import TestClass from './TestClass';
import { useState } from 'react';

function App() {
  const [name, setName] = useState('Avi');
  const [show, setShow] = useState(true);
  const changeProps = () => {
    setName('Nadav');
    setShow(false);
  }
  return (
    <div className="App">
      <button onClick={()=>changeProps()}>Load</button>
      <Test a={1} b={2} name={name}/>
      {
        show ? <TestClass a={1} b={2} name={name}/> : null
      }
    </div>
  );
}

export default App;
