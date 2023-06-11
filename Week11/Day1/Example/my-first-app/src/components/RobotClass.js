import React from 'react';

class RobotClass extends React.Component {
    
    render() {
        const {userinfo} = this.props;
        const {id, name, email} = userinfo;
        return (
        <div>
            <h2>Name:{name}</h2>
            <p>Email:{email}</p>
            <img src={`https://robohash.org/${id}?size=150x150`}/>
        </div>
        )
    }
}

export default RobotClass