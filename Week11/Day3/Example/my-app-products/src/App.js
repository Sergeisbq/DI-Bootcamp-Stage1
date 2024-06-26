import logo from './logo.svg';
import './App.css';
import Products from './components/Products';
import Product from './components/Product';
import { Routes, Route } from 'react-router-dom';



function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Routes>
          <Route path='/' element={<Products />}/>
          <Route path='/:id' element={<Product />}/>
        </Routes>
      </header>
    </div>
  );
}

export default App;
