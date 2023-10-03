// App.js
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Header from './components/Header';
import PetList from './components/PetList';
import PetDetail from './components/PetDetail';

function App() {
  return (
    <Router>
      <div>
        <Header />
        <Switch>
          <Route path="/" exact component={PetList} />
          <Route path="/pets/:id" component={PetDetail} />
          {/* Add more routes here */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;
