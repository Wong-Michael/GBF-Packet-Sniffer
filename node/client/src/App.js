import './App.css';
import GBF from './GBF/GBF';
import {
  BrowserRouter as Router
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <GBF />
      </div>
    </Router>
  );
}

export default App;
