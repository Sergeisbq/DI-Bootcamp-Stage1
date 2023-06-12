import React from 'react';

class CounterC extends React.Component {
    constructor() {
        super();
        this.state = {
            count: 0
        }
        console.log(1, 'constructor');
    }
    handleClick = () => {
        this.setState({count: this.state.count + 1});
        // console.log(this.state.count);
    }

    // componentDidMount = () => {
    //     console.log(3, 'componentDidMount');
    // }

    // componentDidUpdate = () => {
    //     console.log('re-render');
    // }

    render() {
        console.log(2, 'render');
        return (
            <div>
                <h1>Counter:</h1>
                <h2>{this.state.count}</h2>
                <button onClick={this.handleClick}>Add</button>
            </div>
        )
    }
}

export default CounterC