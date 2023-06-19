import {connect} from 'react-redux';
import { changePropOne } from '../redux/actions';

const Test = (props) => {
    return (
        <div>
            <h1>{props.a}</h1>
            <h1>{props.b}</h1>
            <button onClick={()=>props.setTitle('Test Title')}>Change Title</button>
            <div>
                <button onClick={props.change}>Change Prop One</button>
            </div>
        </div>
    )
}

// const mapStateToProps = (state) => {
//     console.log('Store test =>', state);
//     return {
//         a: state.property_one,
//         b: state.property_two,
//     }
// }

// const mapDispatchToProps = (dispatch) => {
//     return {
//         change: () => dispatch(changePropOne('Hello from Test'))
//     }
// }

// export default connect(mapStateToProps, mapDispatchToProps)(Test)
    
