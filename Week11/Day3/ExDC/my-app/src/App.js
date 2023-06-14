import logo from './logo.svg';
import './App.css';
import MyForm from './components/MyForm';
import AppForm from './components/AppForm';

import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import {Routes, Route, Link} from 'react-router-dom';

import React from 'react';


function App() {
  return (
    <div className="App">
      {/* <header className="App-header"> */}
        {/* <MyForm /> */}
        {/* <AppForm /> */}
      {/* </header> */}
      <nav>
        <Link to='/'>Home</Link><br />
        <Link to='/about'>About</Link><br />
        <Link to='/contact'>Contact</Link><br />
      </nav>
      <Routes>
        <Route path='/' element={<Home />}/>
        <Route path='/about' element={<About />}/>
        <Route path='/contact/:id/:pk' element={<Contact />}/>
        <Route path='/contact-about' element={<><Contact /><About /></>}/>
      </Routes>
    </div>
  );
}

export default App;
