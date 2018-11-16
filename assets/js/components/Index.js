import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Button } from 'chramework';

export default class Index extends Component {
    render() {
        return (
            <div className="container px-4 py-4">
                <div className="text-purple">Index Component</div>
                <Button text="Подробнее" arrow bordered />
            </div>
        );
    }
}

if (document.getElementById('index')) {
    ReactDOM.render(<Index />, document.getElementById('index'));
}
