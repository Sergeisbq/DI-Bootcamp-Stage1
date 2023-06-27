import logo from './logo.svg';
import './App.css';
import PhotoContainer from './components/PhotoContainer';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Routes>
          <Route path='/' element={<PhotoContainer />}/>
          <Route path='/' element={<PhotoContainer />}/>
        </Routes>
      </header>
    </div>
  );
}

export default App;
