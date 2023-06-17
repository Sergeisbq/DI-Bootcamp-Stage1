import React from 'react';

class MyForm extends React.Component {
    constructor(props) {
        super(props);
        // this.state = {
        //     value: ''
        // }
    }

    handleSubmit = async (e) => {
        e.preventDefault();
        const inptValue = e.target.elements[0].value;
        const toSend = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({message: inptValue})
        };
        const res = await fetch('http://localhost:3030/api/world', toSend);
        const data = await res.json();
        console.log(data);
        this.props.setMessage(data.message)

    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input type="text"></input>
                <input type="submit" value="Submit"></input>
            </form>
        )
    }
}

export default MyForm