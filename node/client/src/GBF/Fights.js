import React from 'react';
import FightBreakdown from "./FightBreakdown" 
import axios from "axios"
import {Link, Switch, Route, useParams} from "react-router-dom";
class Fights extends React.Component {
    constructor(props) {
        super(props)
        this.state = {fights : []}
    }

    async getServer() {
        axios.get("http://localhost:8080/fights")
        .then(serverResponse => {
            this.setState({
                fights: serverResponse.data
            });

        });
    }

    componentDidMount() {
        this.getServer();
    }

    render() {
        return <div>
            <ul>
                { this.state.fights.map(fight => <li><Link to={fight}>{fight}</Link></li>)}
            </ul>
            <Switch>
                { this.state.fights.map(fightName => <Route exact path={"/" + fightName}><FightBreakdown fight={fightName}/></Route>)}
            </Switch>
        </div>
    }
}


export default Fights