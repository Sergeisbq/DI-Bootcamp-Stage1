import React from 'react';
import Garage from './Garage.js';

class Car extends React.Component {
    constructor() {
        super();
        this.state = {
            color: 'black'
        }
    }
    render() {
        const {carinfo} = this.props;
        const {model, name} = carinfo;

        return (
            <div>
                <h1>This car is {this.state.color} {model}</h1>
                <Garage size="small" />
            </div>
        )
    }
}

export default Car