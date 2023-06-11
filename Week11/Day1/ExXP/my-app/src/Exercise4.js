import React from 'react';
import './Exercise4.css';


class DisplayTags extends React.Component {
    render() {
        const style_header = {
            color: "white",
            backgroundColor: "DodgerBlue",
            padding: "10px",
            fontFamily: "Arial"
          };
        return (
            <>
                <h1 style={style_header}>This is a Header</h1>
                {/* <h1 style={{color: 'red', backgroundColor: 'lightblue'}}>This is a Header</h1> */}
                <p className='para'>This is a Paragraph</p><br/>
                <a href='/'>This is a Link</a><br/>
                <form>
                    <p>This is a Form:</p>
                    <label>Enter your name:</label>
                    <input type="text"></input>
                    <button type="submit">Submit</button>
                </form>
                <img src="https://images.ctfassets.net/dfvzsm9gvxue/3HtsJuzbOALnafhrDk5yvp/b40465ecfccca4856c4269c11be3a1f5/image.png?w=700&h=235&q=50&fm=webp"></img>
                <p>This is a List:</p>
                <div style={{margin: 'auto', width: '100px'}}>
                    <ul>
                        <li>First</li>
                        <li>Second</li>
                        <li>Third</li>
                    </ul>
                </div>
            </>
        )
    }
}

export default DisplayTags


