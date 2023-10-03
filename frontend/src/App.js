// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import PetList from './components/PetList';
import PetDetail from './components/PetDetail';
import Auth from './components/Auth';
import Register from './components/Register';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
        <Header />
          <Route path="/" exact component={PetList} />
          <Route path="/pets/:id" component={PetDetail} />
          <Route exact path="/login" component={Auth} />
          <Route exact path="/register" component={Register} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
