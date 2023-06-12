import React from 'react';
import User from './User';
import Searchbox from './searchbox';

class UserListC extends React.Component {
    constructor() {
        super();
        this.state = {
            arr: [],
            search: ''
        }
    }
    handleClick = () => {
        fetch('https://jsonplaceholder.typicode.com/users')
        .then(res => res.json())
        .then(data => {
            console.log(data);
            this.setState({arr:data})
        })
        .catch(error => {
            console.error(error);
        });
    }

    componentDidMount = () => {
        this.handleClick()
    }

    handleChange = (e) => {
        console.log(e.target.value);
        this.setState({search:e.target.value})
    }

    render() {
        const {search} = this.state;
        const filteredArr = this.state.arr.filter(item => {
            return item.name.toLowerCase().includes(search.toLowerCase())
        })
        return (
                <div>
                    <Searchbox myfunc={this.handleChange} />
                    {/* <div>
                        <input type="text" placeholder='Filter...' onChange={(e) => this.handleChange(e)}/>
                    </div> */}
                {
                    filteredArr.map(item => {
                        return <User userinfo={item} key={item.id} />
                    })
                }
                </div>
        )
    }
}

export default UserListC

