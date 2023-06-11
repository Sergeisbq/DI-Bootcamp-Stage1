import logo from './logo.svg';
import './App.css';
import UserFavoriteColors from './UserFavoriteColors'; 
import DisplayTags from './Exercise4';


function App() {
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals : ['Horse','Turtle','Elephant','Monkey']
  };
  
  const sum = 5 + 5;
  
  const myelement = (
      <div>
          <h1>I Love JSX!</h1> 
          <h1>React is {sum} times better with JSX</h1>
      </div>
  );
  
  const userelement = (
    <div>
        <h3>{user.firstName}</h3> 
        <h3>{user.lastName}</h3>
    </div>
  );
  
  
  const userelement2 = (
    <div> 
        <UserFavoriteColors userinfo = {user} />
    </div>
  );

  const userelement3 = (
    <div> 
        <DisplayTags />
    </div>
  );

  return (
    <div className="App">
      {/* <header className="App-header">

      </header> */}
      {/* <h1>I do not use JSX</h1> */}
      {/* {myelement} */}
      {/* {userelement} */}
      {/* {userelement2} */}
      {userelement3}
    </div>
  );
}

export default App;
