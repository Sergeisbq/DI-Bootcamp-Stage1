import quotes from './QuotesDatabase';
import {useState, useEffect} from 'react';

const Quotes = () => {
    const [num, setNum] = useState(0);
    const [color, setColor] = useState("black");

    //does the job : componenetDidMount,componenetDidupdate, componenetwillunmount
    useEffect( () => {
        console.log("in useeffect");
        document.body.style.backgroundColor = color
    }, [color])

    const randNum = (a, b) => {
        return Math.round(Math.random()*(b - a)) + a;
    }
    
    const randomColor = () => {
        const color = `rgb(
          ${Math.floor(Math.random() * 155)},
          ${Math.floor(Math.random() * 155)},
          ${Math.floor(Math.random() * 155)})`;
        return color;
    }

    const changeinfo = () => {
        let newNum;
        do 
        {
            newNum = randNum(0, 93);
        } 
        while (newNum === num);
        setNum(newNum);

        const color = randomColor();
        setColor(color);
    }

    return (
        <div style={{ color: color, backgroundColor: "white" }}>
            <OneQuote a={num} />
            <button onClick={changeinfo}>New Quote</button>
        </div>
    )
}

const OneQuote = (props) => {
    return (
        <div>
            <h2>{quotes[props.a].quote}</h2>
            <h4>{quotes[props.a].author}</h4>
        </div>
    )
}

export default Quotes
