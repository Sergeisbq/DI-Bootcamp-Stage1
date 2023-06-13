import React from 'react';

class ErrorBoundary extends React.Component {
    constructor() {
        super()
        this.state = {
            hasError: false,
            error: null,
            errorInfo: null,
        }
    }

    componentDidCatch(error, errorInfo) {
        console.log('error=>', error);
        console.log('errorInfo=>', errorInfo);
        this.setState({hasError: true, error: error, errorInfo: errorInfo})
    }

    render() {
        if (this.state.hasError) {
            return (
                <div>
                    Something went wrong we are fixing the problem
                    {this.state.error.message}
                </div>
            )
        }
        return this.props.children
    }
}

export default ErrorBoundary