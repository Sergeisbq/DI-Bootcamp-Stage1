const Robots = (props) => {
    // const {name, email} = props // this way expected to use just 'name' and 'email' in <h2> and <p>
    const {userinfo} = props;
    const {id, name, email} = userinfo;
    return (
        <div>
            <h2>Name:{name}</h2>
            <p>Email:{email}</p>
            <img src={`https://robohash.org/${id}?size=150x150`}/>
        </div>
    )
}

export default Robots