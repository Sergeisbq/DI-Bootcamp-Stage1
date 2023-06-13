import React from 'react';

class ErrorBoundary extends React.Component {
    constructor() {
        super()
        this.state = {
            error: null
        }
    }

    componentDidCatch(error) {
        console.log('error=>', error);
        this.setState({error: error});
    }

    render() {
        if (this.state.error) {
            return (
                <div>
                    Something went wrong
                    <details style={{ whiteSpace: 'pre-wrap' }}>
                        {this.state.error && this.state.error.toString()}
                        <br />
                    </details>
                </div>
            )
        }
        return this.props.children
    }
}

export default ErrorBoundary