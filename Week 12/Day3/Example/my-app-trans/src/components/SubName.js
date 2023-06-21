import {useContext} from 'react';
import { AppContext } from '../App';
import { NameContext } from './Name';


const SubName = (props) => {
    const {setName, count, setCount} = useContext(AppContext)
    const {prompt, setPrompt} = useContext(NameContext)
    return (
        <div>
        {/* <h2>Sub: {name}</h2> */}
            {prompt}
            <input onChange={(e) => setName(e.target.value)}></input>
            <button onClick={(e) => setCount(count + 1)}>Add</button>
        </div>
    )
}

export default SubName