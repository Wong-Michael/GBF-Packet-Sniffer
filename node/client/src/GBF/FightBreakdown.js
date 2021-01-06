import React from 'react';
import {
  PieChart, Pie, Legend, Tooltip,
} from 'recharts';
import axios from "axios"

class FightBreakdown extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      totalDamagePieData: []
    }
  }

  componentDidUpdate(prevProps) {
    if (prevProps.fight != this.props.fight) {
      this.getServer();
    }
  }

  componentDidMount() {
    this.getServer();
  }

  async getServer() {
    axios.get("http://localhost:8080/fight/" + this.props.fight)
      .then(serverResponse => {
        var { total_match, avg_atk_count_match, avg_dmg_match, crit_rate_match } = this.extractData(serverResponse.data);
        var totalData = [
          { name: 'pos_1', value: parseFloat(total_match[1]) },
          { name: 'pos_2', value: parseFloat(total_match[3]) },
          { name: 'pos_3', value: parseFloat(total_match[5]) },
          { name: 'pos_4', value: parseFloat(total_match[7]) }
        ];
        var avg_atk_count_ul = document.getElementById("avg_atk_count")
        var dpt_ul = document.getElementById("dpt")
        var crit_rate_ul = document.getElementById("crit_rate")
        avg_atk_count_ul.innerHTML = ""
        dpt_ul.innerHTML = ""
        crit_rate_ul.innerHTML = ""
        for (var i = 0; i < 4; i++) {
          var avg_atk_li = document.createElement('li')
          avg_atk_li.appendChild(document.createTextNode(avg_atk_count_match[i * 2 + 1]))
          avg_atk_count_ul.appendChild(avg_atk_li)

          var dpt_li = document.createElement('li')
          dpt_li.appendChild(document.createTextNode(avg_dmg_match[i * 2 + 1]))
          dpt_ul.appendChild(dpt_li)

          var crit_rate_li = document.createElement('li')
          crit_rate_li.appendChild(document.createTextNode(crit_rate_match[i * 2 + 1]))
          crit_rate_ul.appendChild(crit_rate_li)
        }
        this.setState({
          totalDamagePieData: totalData
        });
      });
  }

  extractData(dataString) {
    var total = /pos_0_total:([+-]?([0-9]*[.])?[0-9]+) pos_1_total:([+-]?([0-9]*[.])?[0-9]+) pos_2_total:([+-]?([0-9]*[.])?[0-9]+) pos_3_total:([+-]?([0-9]*[.])?[0-9]+) /;
    var avg_atk_count = /pos_0_count_avg:([+-]?([0-9]*[.])?[0-9]+) pos_1_count_avg:([+-]?([0-9]*[.])?[0-9]+) pos_2_count_avg:([+-]?([0-9]*[.])?[0-9]+) pos_3_count_avg:([+-]?([0-9]*[.])?[0-9]+) /;
    var avg_dmg = /pos_0_avg:([+-]?([0-9]*[.])?[0-9]+) pos_1_avg:([+-]?([0-9]*[.])?[0-9]+) pos_2_avg:([+-]?([0-9]*[.])?[0-9]+) pos_3_avg:([+-]?([0-9]*[.])?[0-9]+) /;
    var crit_rate = /pos_0_avg_crit:([+-]?([0-9]*[.])?[0-9]+) pos_1_avg_crit:([+-]?([0-9]*[.])?[0-9]+) pos_2_avg_crit:([+-]?([0-9]*[.])?[0-9]+) pos_3_avg_crit:([+-]?([0-9]*[.])?[0-9]+)/;
    var total_match = dataString.match(total);
    var avg_atk_count_match = dataString.match(avg_atk_count);
    var avg_dmg_match = dataString.match(avg_dmg);
    var crit_rate_match = dataString.match(crit_rate);
    return { total_match, avg_atk_count_match, avg_dmg_match, crit_rate_match };
  }

  render() {
    return (
      <div>
        <h3>FightName: {this.props.fight}</h3>
        <div id="total_pie">
          <PieChart width={800} height={400}>
            <Pie dataKey="value" isAnimationActive={false} data={this.state.totalDamagePieData} cx={200} cy={200} outerRadius={80} fill="#8884d8" label />
            <Tooltip />
          </PieChart>
        </div>
        <h2>Average Attack Count</h2>
        <ul id="avg_atk_count">
        </ul>
        <h2>Average Damage per Turn</h2>
        <ul id="dpt">
        </ul>
        <h2>Average Crit rate</h2>
        <ul id="crit_rate">
        </ul>
      </div>
    );
  }
}

export default FightBreakdown