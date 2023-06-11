const User = (props) => {
    // const {name, email} = props // this way expected to use just 'name' and 'email' in <h2> and <p>
    return (
        <div>
            <h2>Name:{props.name}</h2>
            <p>Email:{props.email}</p>
        </div>
    )
}

export default User