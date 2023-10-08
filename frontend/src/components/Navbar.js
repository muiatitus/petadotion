// Navbar.js

import React from 'react';
import { Link } from 'react-router-dom';

const navStyle = {
  background: '#333',
  color: '#fff',
  padding: '10px',
};

const ulStyle = {
  listStyle: 'none',
  display: 'flex',
  justifyContent: 'space-around',
};

const liStyle = {
  margin: '0',
};

const linkStyle = {
  textDecoration: 'none',
  color: '#fff',
  fontWeight: 'bold',
};

function Navbar({ authenticated, handleAuthentication }) {
  // Function to handle user logout
  const handleLogout = async () => {
    // Implement your logout logic here, e.g., clear user tokens or cookies
    // You should replace this with your actual logout logic.

    // Clear the authentication status
    handleAuthentication(false);
  };

  return (
    <nav style={navStyle}>
      <ul style={ulStyle}>
        <li style={liStyle}>
          <Link to="/" style={linkStyle}>
            Home
          </Link>
        </li>
        <li style={liStyle}>
          <Link to="/pets" style={linkStyle}>
            Pets
          </Link>
        </li>
        <li style={liStyle}>
          <Link to="/profile" style={linkStyle}>
            Edit Profile
          </Link>
        </li>
        <li style={liStyle}>
          <Link to="/pet-form" style={linkStyle}>
            Pet Form
          </Link>
        </li>
        {authenticated ? (
          <li style={liStyle}>
            <Link to="/logout" onClick={handleLogout} style={linkStyle}>
              Logout
            </Link>
          </li>
        ) : (
          <React.Fragment>
            <li style={liStyle}>
              <Link to="/login" style={linkStyle}>
                Login
              </Link>
            </li>
            <li style={liStyle}>
              <Link to="/register" style={linkStyle}>
                Register
              </Link>
            </li>
          </React.Fragment>
        )}
      </ul>
    </nav>
  );
}

export default Navbar;
