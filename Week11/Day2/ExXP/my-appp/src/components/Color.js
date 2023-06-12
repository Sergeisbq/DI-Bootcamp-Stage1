import React from 'react';


class Color extends React.Component {
    constructor() {
        super();
        this.state = {
            color: "red"
        };
    }
    componentDidMount() {
        setTimeout(() => {
            this.setState({color: 'yellow'});
        }, 5000);
    }
    
    clickMe = () => {
        this.setState({color: 'blue'}); 
    }

    render() {
        return (
            <div>
                <h1>My Favorite Color is {this.state.color}</h1>
                <button onClick={this.clickMe}>Change color</button>
            </div>
        )
    }
}

export default Color