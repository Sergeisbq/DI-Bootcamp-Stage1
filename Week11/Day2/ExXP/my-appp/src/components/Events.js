import React from 'react';

class Event extends React.Component {
    
    constructor() {
        super();
        this.state = {
            isToggleOn: true
        }
    }
    
    clickMe = () => {
        alert('I was clicked');
    }

    handleKeyDown = (event) => {
        if (event.key === 'Enter') {
          event.preventDefault();
          alert(`You pressed Enter with input value: ${event.target.value}`);
        }
      };

    clickMeStatus = (event) => {
        event.preventDefault();
        if (this.state.isToggleOn === true) {
            this.state.isToggleOn = false;
            const btn = document.getElementById('On/Off');
            btn.textContent = 'OFF'
        }
        else {
            this.state.isToggleOn = true;
            const btn = document.getElementById('On/Off');
            btn.textContent = 'ON'
        }
        console.log(this.state.isToggleOn);
    }
    render () {
        return (
            <div>
                <input type="text" onKeyDown={this.handleKeyDown} />
                <button onClick={this.clickMe}>clickMe</button>
                <button id="On/Off"onClick={this.clickMeStatus}>On/Off</button>
            </div>
        )
    }
}

export default Event