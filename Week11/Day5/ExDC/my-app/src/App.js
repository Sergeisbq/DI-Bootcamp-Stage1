import logo from './logo.svg';
import './App.css';
import React from 'react';
import heroes from './superheroes.json'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      heroes: heroes.superheroes,
      clcHeroes: [],
      score: 0,
      topScore: 0
    }
  }

  handleClick = (nameH) => {
    this.setState((state) => {
      const newScore = state.clcHeroes.includes(nameH) ? 0 : state.score + 1;
      const clcHeroes = state.clcHeroes.includes(nameH) ? [] : [...this.state.clcHeroes, nameH];
      return {
        heroes: [...this.state.heroes].sort((a, b) => (Math.random() > 0.5 ? -1 : 1)),
        clcHeroes: clcHeroes,
        score: newScore,
        topScore: Math.max(newScore, state.topScore)
      }
    });
  };
  

  render() {
    return (
      <div className="App">
        <nav>
          <h1>Superheroes Memory Game</h1>
          <div>Score: {this.state.score}</div>
          <div>Top Score: {this.state.topScore}</div>
        </nav>
        <h1>Get points by clicking on an image but don't click on any more than once!</h1>
        <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: "3rem"}}>
          {this.state.heroes.map((item) => {
            return(
              <div key={item.id} onClick={() => this.handleClick(item.name)}>
                <h4>{item.name}</h4>
                <p>{item.occupation}</p>
                <img src={item.image} width={"200px"}></img>
              </div>
            )
          })}
        </div>
      </div>
    );
  }

}

export default App;
