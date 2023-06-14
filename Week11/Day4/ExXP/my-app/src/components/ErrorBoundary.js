import React from 'react';

class ErrorBoundary extends React.Component {
    constructor() {
        super()
        this.state = {
            hasError: false
        }
    }

    componentDidCatch(hasError) {
        console.log('hasError=>', hasError);
        this.setState({hasError: true});
    }

    render() {
        // throw Error('Error')
        if (this.state.hasError) {
            return (
                <div>
                    Something went wrong
                </div>
            )
        }
        return this.props.children
    }
}

export default ErrorBoundary