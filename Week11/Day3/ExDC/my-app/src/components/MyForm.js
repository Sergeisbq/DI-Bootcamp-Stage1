import React from 'react';

class MyForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstname: '',
      lastname: '',
      age: '',
      selOptGen: '',
      selOptDest: '',
      selOptDiet: '',
    };
  }

  handleChange = (e) => {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    const { firstname, lastname, age, selOptGen, selOptDest, selOptDiet } = this.state;
//     const queryString = new URLSearchParams({
//         firstname,
//         lastname,
//         age,
//         selOptGen,
//         selOptDest,
//         selOptDiet,
//       }).toString();
//       const url = `http://localhost:3000/?${queryString}`;
//       window.location.href = url;
  };


  handleOptionGen = (e) => {
    this.setState({ selOptGen: e.target.value });
  };

  handleOptionDest = (e) => {
    this.setState({ selOptDest: e.target.value });
  };

  handleOptionDiet = (e) => {
    this.setState({ selOptDiet: e.target.value });
  };

  render() {
    const { firstname, lastname, age, selOptGen, selOptDest, selOptDiet } = this.state;

    return (
      <div>
        <form onSubmit={this.handleSubmit}>
            <input type="text" name="firstname" placeholder="First Name" value={firstname} onChange={this.handleChange} />
            <input type="text" name="lastname" placeholder="Last Name" value={lastname} onChange={this.handleChange} />
            <input type="text" name="age" placeholder="Age" value={age} onChange={this.handleChange}/>
            <br />
            <h4>Gender</h4>
            <label htmlFor="male">Male</label>
            <input type="radio" name="male" value="male" onChange={this.handleOptionGen} checked={selOptGen === 'male'} />
            <label htmlFor="female">Female</label>
            <input type="radio" name="female" value="female" onChange={this.handleOptionGen} checked={selOptGen === 'female'} />
            <br />
            <br />
            <label htmlFor="destination">Destination:</label>
            <select name="destination" id="destination" value={selOptDest} onChange={this.handleOptionDest}>
                <option value="Thailand">Thailand</option>
                <option value="Japan">Japan</option>
                <option value="Brasil">Brasil</option>
            </select>
            <h4>Dietary restrictions</h4>
            <label htmlFor="destination">Nuts Free</label>
            <input type="checkbox" name="nuts" value="NutsFree" onChange={this.handleOptionDiet} checked={selOptDiet === 'NutsFree'}/>
            <label htmlFor="destination">Lactose Free</label>
            <input type="checkbox" name="lactose" value="LactoseFree" onChange={this.handleOptionDiet} checked={selOptDiet === 'LactoseFree'} />
            <label htmlFor="destination">Vegan</label>
            <input type="checkbox" name="vegan" value="Vegan" onChange={this.handleOptionDiet} checked={selOptDiet === 'Vegan'} />
            <br />

          <button type="submit">Submit</button>
        </form>

        <div>
          <h2>Form Values:</h2>
          <p>First Name: {firstname}</p>
          <p>Last Name: {lastname}</p>
          <p>Age: {age}</p>
          <p>Gender: {selOptGen}</p>
          <p>Destination: {selOptDest}</p>
          <p>Dietary restrictions: {selOptDiet}</p>
        </div>
      </div>
    );
  }
}

export default MyForm;



