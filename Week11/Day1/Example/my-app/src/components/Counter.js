import { useState, useEffect } from 'react';

const Counter = (props) => {

    const [count, setCount] = useState(0);
    const [name, setName] = useState('')
    // const [state, setState] 

    useEffect(() => {
        console.log(count);
    }, [name])

    const handleClick = () => {

        setCount(count + 1)
    }
    return (
        <div>
            <h1>Counter:</h1>
            <h2>{count}</h2>
            <input type="text" onChange={(e)=>setName(e.target.value)} />
            <button onClick={handleClick}>Add</button>
        </div>
    )
}

export default Counter