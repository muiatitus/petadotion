import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Header from './components/Header';
import PetList from './components/PetList';
import PetDetail from './components/PetDetail';
import Auth from './components/Auth';
import Register from './components/Register';
import Login from './components/Login';
import AdminLogin from './components/AdminLogin';
import AdminRoutes from './components/adminRoutes';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/pets/:id" element={<PetDetail />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route exact path="/adminLogin" element={<AdminLogin/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;