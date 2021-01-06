import React from 'react';
import ReactDOM from 'react-dom';
import axios from "axios"
import Fights from "./Fights"
class GBF extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return <div>
            <h1>GBF Battle Reviewer</h1>
            <Fights />
        </div>
    }
}

export default GBF;