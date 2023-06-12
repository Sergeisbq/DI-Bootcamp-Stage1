import React from 'react';

class Garage extends React.Component {
    constructor() {
        super();
    }
    render() {
        const {size} = this.props;

        return (
            <div>
                <h1>Who lives in my {size} Garage?</h1>
            </div>
        )
    }
}

export default Garage