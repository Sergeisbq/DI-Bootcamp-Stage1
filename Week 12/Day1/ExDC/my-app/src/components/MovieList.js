import React from 'react';
import {connect} from 'react-redux';
import { changePropOne } from '../redux/actions';
import { selectMovie } from './MovieDetails';
import MovieDetails from './MovieDetails';



class MovieList extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div>
                <h1>Movie List</h1>
                {this.props.movies.map((item, i) => (
                    <div key={i}>
                        <span>{item.title}</span>
                        <button onClick={()=>this.props.handleClick(item)}>details</button>
                    </div>
                ))}
                <MovieDetails />
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        movies: state.movies,
    } 
};

const mapDispatchToProps = (dispatch) => {
    return {
        handleClick: (movie) => dispatch(selectMovie(movie)),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(MovieList);