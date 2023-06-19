import React from 'react';
import {connect} from 'react-redux';
import { changePropOne } from '../redux/actions';


export const selectMovie = (title) => ({
    type: "SEL", title
})

class MovieDetails extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>Movie Details
                {this.props.selectedMovie !== null && 
                <div><p>{this.props.selectedMovie.title}</p>
                <p>{this.props.selectedMovie.releaseDate}</p> 
                <p>{this.props.selectedMovie.rating}</p></div>
                }
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    selectedMovie: state.selectedMovie,
});

export default connect(mapStateToProps)(MovieDetails)