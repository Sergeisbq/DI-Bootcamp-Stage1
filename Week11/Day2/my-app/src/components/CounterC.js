import React from 'react';

class CounterC extends React.Component {
    constructor() {
        super();
        this.state = {
            languages : [
                {name: "Php", votes: 0},
                {name: "Python", votes: 0},
                {name: "JavaSript", votes: 0},
                {name: "Java", votes: 0}
            ]
        }
    }
    handleClick0 = () => {
        const newVotes = [...this.state.languages];
        newVotes[0].votes += 1;
        this.setState({ languages: newVotes });
    }

    handleClick1 = () => {
        const newVotes = [...this.state.languages];
        newVotes[1].votes += 1;
        this.setState({ languages: newVotes });
    }

    handleClick2 = () => {
        const newVotes = [...this.state.languages];
        newVotes[2].votes += 1;
        this.setState({ languages: newVotes });
    }

    handleClick3 = () => {
        const newVotes = [...this.state.languages];
        newVotes[3].votes += 1;
        this.setState({ languages: newVotes });
    }

    render() {
        return (
            <div>
                <h1>Vote Your Language!</h1>
                <h2>{this.state.languages[0].name} {this.state.languages[0].votes} <button onClick={this.handleClick0}>Vote</button></h2>
                <h2>{this.state.languages[1].name} {this.state.languages[1].votes} <button onClick={this.handleClick1}>Vote</button></h2>
                <h2>{this.state.languages[2].name} {this.state.languages[2].votes} <button onClick={this.handleClick2}>Vote</button></h2>
                <h2>{this.state.languages[3].name} {this.state.languages[3].votes} <button onClick={this.handleClick3}>Vote</button></h2>
            </div>
        )
    }
}

export default CounterC