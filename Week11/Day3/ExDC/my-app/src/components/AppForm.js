import React from 'react'

class AppForm extends React.Component {
    constructor() {
        super();
        this.state = {
            firstname: '',
            lastname: '',
            color: '',
            isgo: '',
            gender: ''
        }
    }
    
    // huks
    // const [FormData, setFormData] = useState({
    //     firstname: 'aa',
    //     lastname: 'aa',
    //     color: 'aa',
    //     isgo: 'aa',
    //     gender: 'aa'
    // });

    handleSubmit = (e) => {
        e.preventDefault();
        const { firstname, lastname, color, isgo, gender } = this.state;
        const go = isgo ? 'Yes, I am going' : 'No way';
        console.log(firstname, lastname, color, go, gender);
    }

    handleChange = (e) => {
        // console.log(e.target.value);
        // console.log(e.target.checked);
        const value = (e.target.type === 'checkbox')
                        ? e.target.checked 
                        : e.target.value;
        this.setState({[e.target.name]: value})

        // huks
        // setFormData({...formData, [e.target.name]:value})
    }

    render() {
        return (
            <>
                <h1>My Form</h1>
                <form onSubmit={this.handleSubmit}>
                    First Name: <input type="text" name="firstname" onChange={this.handleChange} /><br />
                    Last Name: <input type="text" name="lastname" onChange={this.handleChange}/><br />

                    <select name="color" onChange={this.handleChange} >
                        <option value="1">Red</option>
                        <option value="2">Blue</option>
                        <option value="3">Green</option>
                    </select>
                    
                    <br />

                    Is going: <input type="checkbox" value="ISGO" name="isgo" onChange={this.handleChange} />

                    <br />

                    <div onChange={this.handleChange}>
                        <input type="radio" value="Male" name="gender" /> Male
                        <input type="radio" value="Male" name="gender" /> Female
                        <input type="radio" value="Male" name="gender" /> Other
                    </div>

                    <input type="submit" value="Submit" />
                </form>
            </>
        )
    }
}

export default AppForm

// let a = 'name'

// let obj = {
//     [a]: "John"
// }