import React from 'react';

class Clock extends React.Component {
    constructor() {
        super();
        const temp1 = new Date();
        const date1 = temp1.toTimeString();
        this.state = {
            currentDate: date1
        }
    }

    componentDidMount() {
        setInterval(() => {
            this.setState({currentDate: new Date().toTimeString()});
        }, 1000);
    }

    render() {
        return (
            <div>
                <h1>Now is {this.state.currentDate}</h1>
            </div>
        )
    }
}

export default Clock