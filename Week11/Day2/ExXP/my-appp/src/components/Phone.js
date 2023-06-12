import React from 'react';


class Phone extends React.Component {
    constructor() {
        super();
        this.state = {
            brand: "Samsung",
            model: "Galaxy S20",
            color: "black",
            year: 2020
        };
    }

    clickMe = () => {
        this.setState({color: 'blue'});
    }

    render() {

        return (
            <div>
                <h1>My phone is {this.state.brand}</h1>
                <h2>It is a {this.state.color} {this.state.model} from {this.state.year}</h2>
                <button onClick={this.clickMe}>Change color</button>
            </div>
        )
    }
}

export default Phone