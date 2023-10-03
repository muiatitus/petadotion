// Header.js
import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        {/* Add more navigation links */}
      </ul>
    </nav>
  );
}

export default Header;
