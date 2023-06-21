import logo from './logo.svg';
import './App.css';
import TransactionList from './components/TransactionList';
import { createContext, useState } from 'react';
import Name from './components/Name';

// function App() {
//   return (
//     <div className="App">
//       <TransactionList />
//     </div>
//   );
// }

// export default App;


export const AppContext = createContext(null);

function App() {

  const [name, setName] = useState('John')
  const [count, setCount] = useState(0)

  return (
    <AppContext.Provider value={{name, setName, count, setCount}}>
      <div>
        <h1>useContext</h1>
        <Name />
      </div>
    </AppContext.Provider>
)
}

export default App;
