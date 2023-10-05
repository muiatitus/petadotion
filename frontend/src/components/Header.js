import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <nav className="header"> {/* Add the "header" class */}
      <Link to="/" className="header-link">Home</Link>
      <Link to="/login" className="header-link">Login</Link>
      <Link to="/register" className="header-link">Register</Link>
    </nav>
  );
}

export default Header;