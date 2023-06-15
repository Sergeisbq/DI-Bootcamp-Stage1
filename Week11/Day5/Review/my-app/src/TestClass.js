import React from 'react';

class TestClass extends React.Component{
    constructor(props) {
        super(props)
        this.state = {
            name: props.name,
            arr: []
        }
        // let arr = []
        // console.log(this.props);
    }

    loadarr = () => {
        let data = [
            {name: 'Avi'}, {name: 'Zivuch'}, {name: 'Elena'}
        ]
        // this.state.arr = data
        console.log(this.state.arr);
        this.setState({arr:data})
    }

    componentDidMount = () => {
        console.log(this.state);
    }

    componentDidUpdate = (prevProps, prevState) => {
        console.log(prevProps, this.props);
        // if (this.state.arr[0].name != prevState.state.arr[0].name){
        //     console.log(this.state.arr[0].name);
        // }
    }

    componentWillUnmount = () => {
        alert("Don't do that")
    }

    render() {
        console.log(this.props);
        return (
            <>
            <h1>{this.props.name}</h1>
            <button onClick={this.loadarr}>Load</button>
                {
                    this.state.arr.map(item => {
                        return <div>{item.name}</div>
                    })
                }
            </>
        )
    }
}

export default TestClass