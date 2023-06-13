import React from 'react';


class Colors extends React.Component {
    constructor() {
        super();
        this.state = {
            color: "red",
        };
    }

    componentDidMount() {
        console.log("in mount");
        setTimeout(() => {
            //this.state.color = "yellow" //never do --> if you want to change the state : setState
            //because you want to rerender
            // if you don't use setState you change without rerendering
            this.setState({color: 'yellow'});
        }, 1000);
    }

    // shouldComponentUpdate() {
    //     return (false)
    // }

    componentDidUpdate() {
        console.log("after update")
        // setTimeout(() => {
            // this.setState({color: 'green'});
            // let span =  document.getElementById("spanone")
            // span.textContent = this.state.color;
        // }, 1000);
    }
    
    getSnapshotBeforeUpdate() {
        console.log("in getSnapshotBeforeUpdate")
    }

    clickMe = () => {
        this.setState({color: 'blue'}); 
    }

    render() {
        console.log("in the render");
        return (
            <div>
                <h1>My Favorite Color is <span id="spanone">{this.state.color}</span></h1>
                <button onClick={this.clickMe}>Change color</button>
            </div>
        )
    }
}

export default Colors