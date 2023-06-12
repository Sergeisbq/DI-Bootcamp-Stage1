import React from 'react';
import Input from './Input';

class From extends React.Component {
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
                <form>
                    <label>First name</label>
                    <Input />
                    <label>Last name</label>
                    <Input />
                    <label>Phone</label>
                    <Input />
                    <label>Email</label>
                    <Input />
                    <button type='submit'>Submit</button>
                </form>
            </div>
        )
    }
}

export default From