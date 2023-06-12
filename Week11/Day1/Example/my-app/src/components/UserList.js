import User from './User';
import { useState, useEffect } from 'react';

const UserList = (props) => {
    const [arr, setArr] = useState([]);
    useEffect(() => {
        getUsers()
    }, [])

    const getUsers = () => {
        fetch('https://jsonplaceholder.typicode.com/users')
        .then(res => res.json())
        .then(data => {
            console.log(data);
            setArr(data)
        })
        .catch(error => {
            console.error(error);
        });
    }

    return (
        <div>
            {
            arr.map(item => {
                return <User userinfo={item} key={item.id} />
            })
            }
        </div>
        // <button onClick={handleClick}>Get Users</button>
    )
}

export default UserList