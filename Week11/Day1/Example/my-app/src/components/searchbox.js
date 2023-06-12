const Searchbox = (props) => {
    // console.log(props);
    const {handleChange} = props
    return (
        <div>
            <input type="text" placeholder='Filter...' onChange={(e)=>props.myfunc(e)}/>
        </div>
    )
}

export default Searchbox