import React from 'react';

const usersUrl = "https://jsonplaceholder.typicode.com/users";
const imageUrl = "https://robohash.org/1?size=200x200";

export default class Robot extends React.Component {
    
    render() {
        return(
            <div className="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
                <img alt="robots" src="https://robohash.org/1?size=200x200" />
                <div>
                    <h2>Leanne Graham</h2>
                    <p>Sincere@april.biz</p>
                </div>
            </div>
        )
    }
}