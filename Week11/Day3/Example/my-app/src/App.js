import logo from './logo.svg';
import './App.css';
import Parent from './components/Parent';
import Child from './components/Child';
import Counter from './components/Counter';
import ErrorBoundary from './ErrorBoundary';
import { useState } from 'react';

function App() {
  // const [name, setName] = useState('John');

  const handleSubmit = (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form)


    const formJason = Object.fromEntries(formData.entries())
    console.log(formJason);

    fetch('./some-api', 
    {method: form.method, 
      body: {
        name: e.target.name.value,
        username: e.target.username.value
      }
    })
    



    // console.log('formData=>', formData);
    // You can pass formData 
    // fetch('./some-api', {method: form.method, body: formData})

    // Or with plain Object

    // const formJason = Object.fromEntries(formData.entries()) // formJason put in body above
    // console.log('formJason=>', formJason);
    // console.log(formData.entries());
  }
  return (
    <div className="App">
      <header className="App-header">

        {/* <Parent username='zivuch'>
          <Child />
        </Parent> */}

        {/* <ErrorBoundary>
          <Counter />
        </ErrorBoundary>
        
        <Counter /> */}

        <form onSubmit={handleSubmit} method="POST">
          <label>
          name: <input type="text" name="name"
          //  onChange={(e)=>setName(e.target.value)}
           />
           </label>
           <label>
          name: <input type="text" name="username"/>
           </label>
          <input type="submit" value="Send" />
        </form>
        {/* {name} */}

      </header>
    </div>
  );
}

export default App;
