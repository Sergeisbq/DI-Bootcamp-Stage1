import React from 'react';

class RobotClass extends React.Component {
    
    render() {
        const {userinfo} = this.props;
        const {id, name, email, username, phone} = userinfo;
        return (
        <div className='tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5'>
            <h2>{name}</h2>
            <p>{email}</p>
            <p>{username}</p>
            <p>{phone}</p>
            <img src={`https://robohash.org/${id}?size=150x150`}/>
        </div>
        )
    }
}

export default RobotClass