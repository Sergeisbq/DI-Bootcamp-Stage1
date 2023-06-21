import './App.css';
import { createContext, useState, useRef } from 'react';

function App() {
    let count = useRef(0)

    const userName = useRef(null)
    const div = useRef(null)

    const addOne = () => {
        // count.current = count.current + 2
        // console.log(count.current);
        console.log(userName.current.value);
        userName.current.focus()
        div.current.style.color = 'green'
    }
    return (
        <div className="App" ref={div}>
            <input ref={userName} />
            <h1>useRef</h1>
            <button onClick={addOne}>Add to Ref</button>
        </div>
    );
}

export default App;

