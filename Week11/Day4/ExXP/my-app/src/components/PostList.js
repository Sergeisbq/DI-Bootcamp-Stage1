import data from '../posts.json';
import React from 'react';

class PostList extends React.Component {
    constructor() {
        super()
        this.state = {
            posts: data
        }
    }

    render() {
        return (
            <div>
                <h1>Posts</h1>
                    {this.state.posts.map(post => (
                        <div key={post.id}>
                            <p><b>{post.title}</b></p>
                            <p>{post.content}</p>
                        </div>
                    ))}
            </div>
        )
    }
}

export default PostList
