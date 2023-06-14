import logo from './logo.svg';
import './App.css';
import ErrorBoundary from './components/ErrorBoundary';
import { BrowserRouter, Router, Routes, Route, NavLink, Link } from "react-router-dom";
import Home from './components/Home';
import Profile from './components/Profile';
import Shop from './components/Shop';
import PostList from './components/PostList.js';
import DataList1 from './components/Example1';
import DataList2 from './components/Example2';
import DataList3 from './components/Example3';
import "bootstrap/dist/css/bootstrap.min.css";
import React from 'react';



// function App() {

//   return (
//     <div className="App">

//       <BrowserRouter>
//         <nav bg="dark" variant="dark" expand="lg">
//           <NavLink to='/'>Home</NavLink>
//           <NavLink to='/profile'>Profile</NavLink>
//           <NavLink to='/shop'>Shop</NavLink>
//           <NavLink to='/posts'>Posts</NavLink>
//           <NavLink to='/ex1'>Example1</NavLink>
//           <NavLink to='/ex2'>Example2</NavLink>
//           <NavLink to='/ex3'>Example3</NavLink>
//         </nav>

//         <Routes>
//           <Route path='/' element={<ErrorBoundary><Home /></ErrorBoundary>}>Home</Route>
//           <Route path='/profile' element={<ErrorBoundary><Profile /></ErrorBoundary>}>Profile</Route>
//           <Route path='/shop' element={<ErrorBoundary><Shop /></ErrorBoundary>}>Shop</Route>
//           <Route path='/posts' element={<PostList />}>Posts</Route>
//           <Route path='/ex1' element={<DataList1 />}>Example1</Route>
//           <Route path='/ex2' element={<DataList2 />}>Example2</Route>
//           <Route path='/ex3' element={<DataList3 />}>Example3</Route>
//         </Routes>
        
//       </BrowserRouter>

//       <button onClick={this.postData}>Fetch Data</button>

//     </div>
//   );
// }


class App extends React.Component {
  postData = async() => {
    try {
      const data = {
          key1: 'myusername',
          email: 'mymail@gmail.com',
          name: 'Isaac',
          lastname: 'Doe',
          age: 27
      };

      const response = await fetch('https://webhook.site/5e12f2fe-c8a6-48b2-9917-81f6efeab638', {
        method: 'post',
        mode: 'no-cors',
        headers: {
              'Accept': 'application/json',
              'Content-type': 'application/json' 
            },
        body: JSON.stringify(data),

      });

      console.log(response);
    }
    
    catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        <button onClick={this.postData}>Fetch Data</button>
      </div>
    );
  }
}

export default App;
