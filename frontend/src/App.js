import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'; // Import your app-wide styles here
import Home from './components/Home';
import PetList from './components/PetList';
import PetDetail from './components/PetDetail';
import NotFound from './components/NotFound';
import Register from './components/Auth/Register';
import Navbar from './components/Navbar.js';

// Import the new components for Edit Profile and Pet Form
import Profile from './components/Auth/Profile';
import PetForm from './components/PetForm';
import Login from './components/Auth/Login';

function App() {
  const [authenticated, setAuthenticated] = useState(false); // Initialize as false

  // Function to handle user authentication status
  const handleAuthentication = (status) => {
    setAuthenticated(status);
  };

  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <Navbar authenticated={authenticated} handleAuthentication={handleAuthentication} />
          <h1>Pet Adoption App</h1>
        </header>

        <Routes>
          {/* Define your routes here */}
          <Route
            exact
            path="/register"
            element={<Register handleAuthentication={handleAuthentication} />}
          />
          <Route
            exact
            path="/login"
            element={<Login handleAuthentication={handleAuthentication} />}
          />
          <Route exact path="/" element={<Home authenticated={authenticated} />} />
          <Route exact path="/pets" element={<PetList />} />
          <Route path="/pets/:id" element={<PetDetail />} />
          {/* Add routes for Edit Profile and Pet Form */}
          <Route
            exact
            path="/profile"
            element={<Profile authenticated={authenticated} />}
          />
          <Route
            exact
            path="/pet-form"
            element={<PetForm authenticated={authenticated} />}
          />

          <Route element={<NotFound />} />
        </Routes>

        <footer>
          {/* Your footer content goes here */}
          <p>&copy; 2023 Pet Adoption App</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
