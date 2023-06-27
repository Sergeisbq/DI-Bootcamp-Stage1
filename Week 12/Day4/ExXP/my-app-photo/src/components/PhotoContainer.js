import {useState, useEffect} from 'react';
import {useParams, Link, useNavigate} from 'react-router-dom';
import Photo from './Photo';

const PhotoContainer = (props) => {
    const [photo, setPhoto] = useState([]);
    const [param, setParam] = useState('');

    // const [data, setData] = useState([]);
    // const param = useParams();
    // const navigate = useNavigate();


    // useEffect(() => {
    //     getProductInfo()
    // }, [])

    const getPhotos = async(e) => {
        e.preventDefault()

        setParam(e.target.elements.handInp.value);
        const inpVal = e.target.elements.handInp.value
        try {
            const res = await fetch(`https://api.pexels.com/v1/search/?query=${inpVal}&per_page=30`, {
                headers: {
                  Authorization: "uOMcIuQQUpA43uqWya8DxDxrkvd8XD1BPT85WVRtw6BNPcTzAejrcW0h"
                }
            })
            
            const data = await res.json();
            console.log(data.photos);
            setPhoto(data.photos);
            
        }
        catch (e) {
            console.log(e);
        }
    }



    return (
        <div className='main-container'>
            <div>
                <form onSubmit={getPhotos}>
                        <input name="handInp" type="text" onChange={(e) => setParam(e.target.value)}></input>
                        <button type="submit" >Search</button>
                        <br />
                        <button type="submit" >Mountain</button>
                        <button type="submit" >Beaches</button>
                        <button type="submit" >Birds</button>
                        <button type="submit" >Food</button>
                </form>
            </div>
            <div className='photo-container'>
                <Photo photos={photo}/>
            </div>
            {/* { 
                photo.map(item => {
                    return (
                        <div key={item.id}>
                            <img src={item.src.medium} alt='img' width={'100px'} height={'100px'}></img>

                        </div>
                    )
                })
            } */}
        </div>
    )
}

export default PhotoContainer