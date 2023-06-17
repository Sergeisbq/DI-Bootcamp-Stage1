import logo from './logo.svg';
import './App.css';
import React from 'react';
import MyForm from './components/MyForm';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      message: null
    }
  }
  async componentDidMount() {
    try {
      const res = await fetch('http://localhost:3030/api/hello');
      const data = await res.text();
      console.log(data);
      this.setState({message: data})
    }
    catch (e) {
      console.log(e);
    }
  }
  render() {
    return (
      <div>
        <MyForm setMessage={(message) => this.setState({message: message})}/>
        <h1>{this.state.message}</h1>
      </div>
    )
  }
}

export default App;
