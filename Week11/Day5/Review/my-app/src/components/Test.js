import { useState, useEffect } from 'react';

const Test = (props) => {

    const [arr, setArr] = useState(null);
    // const [state, setState] === this.state.arr in TestClass

    useEffect(() => {
        console.log(arr, props.name);
        return () => {
            console.log('aaa');
        }
    }, [arr, props.name])

    const loadarr = () => {
        let data = [
            {name: 'Avi'}, {name: 'Zivuch'}, {name: 'Elena'}
        ]
        setArr(data);
    }

    return (
        <div>
            <h1>Hello from Test</h1>
            <button onClick={loadarr}>Load</button>
            {
                arr ? arr.map((item, i) => {
                    return <div key={i}>{item.name}</div>
                }) : null
            }
        </div>
    )
}

export default Test