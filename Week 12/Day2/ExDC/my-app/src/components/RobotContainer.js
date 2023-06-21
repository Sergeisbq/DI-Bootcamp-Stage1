import React from 'react';
import Robot from './Robot';
// import {connect} from 'react-redux';
import {useSelector} from 'react-redux';

const RobotContainer = () => {
    const users = useSelector(globalstate => globalstate.users)
    const inputvalue = useSelector(globalstate => globalstate.inputValue)

    return(
        <div className="robot-container">
            {users
                .filter(user => user.name.toLowerCase().includes(inputvalue?.toLowerCase() || ''))
                .map((item) => (
                    <Robot key={item.id} name={item.name} email={item.email} id={item.id}/>
            ))}
        </div>
        )
}

export default RobotContainer