import React from 'react';

class ToDo extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            tasks: ['one', 'two', 'three']
        }
    }

    addTask = (e) => {
        e.preventDefault();
        const value = e.target.elements.task.value;
        console.log(value);
        this.setState({tasks: [...this.state.tasks, value]});
        console.log(this.state.tasks);
        e.target.elements.task.value = '';
    }

    delTask = (e) => {
        console.log(e);
        const idx = e.target.parentElement.id
        console.log("idx", idx);
        let newArray = [...this.state.tasks]
        newArray = newArray.filter((item, id) => idx != id)
        console.log("newArray", newArray);
        this.setState({tasks: newArray});
    }

    render() {
        return (
            <div>
                <form onSubmit={this.addTask}>
                    <input id="task" type="text" />
                </form>
                {this.state.tasks.map((item, i) => {
                    return (
                        <div onClick={this.delTask} id={i} key={i}>
                            <h1>{item}</h1>
                        </div>
                    )
                })
                }   
            </div>
        )
    }
}

export default ToDo