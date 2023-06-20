import logo from './logo.svg';
import './App.css';
import TransactionForm from './components/TransactionForm';
import TransactionList from './components/TransactionList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <TransactionForm />
        <TransactionList />
      </header>
    </div>
  );
}

export default App;
