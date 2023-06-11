import './Hello.css';
import React from 'react';
import HelloClass from './HelloClass';

const Hello = () => {
    const users = [
    {
        name: 'Mary',
        email: 'mary@gmail.com',
        id: 1
    },
    {
        name: 'John',
        email: 'john@gmail.com',
        id: 2
    },
    {
        name: 'David',
        email: 'david@gmail.com',
        id: 3
    }
]

    const returnusers = users.map(item => { // or just index ((item, i) => { return ( <div key={i}.........)})
        return (
        <div key={item.id} style={{
            textAlign:'center',
            display: 'inline-block',
            padding: '20px',
            margin: '20px',
            border: '1px solid black'
            }}>
            <h4 className="title">{item.name}</h4>
            <p>{item.email}</p>
        </div>
            )
    })
return (
    // <React.Fragment> === <>
    <div> 
        <h1> Hello,</h1>
        {
            returnusers
        }
        <HelloClass />
    </div>
    // </React.Fragment> === </>
    )
}

export default Hello