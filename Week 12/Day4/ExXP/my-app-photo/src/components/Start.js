import {useContext, createContext, useState} from 'react';
import { AppContext } from '../App';
import SubName from './SubName';


export const NameContext = createContext(null);

const Start = (props) => {
    const [prompt, setPrompt] = useState('Hello from prompt')
    const {name, count} = useContext(AppContext);
    return (
        <div>
            <h2>My Name: {name}</h2>
            <h2>Count: {count}</h2>
            <NameContext.Provider value={{prompt}}>
                <SubName />
            </NameContext.Provider>
        </div>
    )
}

export default Start