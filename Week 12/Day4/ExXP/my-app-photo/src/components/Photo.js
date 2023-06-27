import {useState, useEffect} from 'react';
import {useParams, Link, useNavigate} from 'react-router-dom';


const Photo = (props) => {
    console.log(props);
    return (
        props.photos.map(item => {
            return (
                <div>
                    <ul>
                        <li key={item.id}>
                            <img src={item.src.medium} alt='img'></img>
                        </li>
                    </ul>
                </div>
            )
        })
    )
        

}

export default Photo

