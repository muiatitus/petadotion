import React from 'react';

function Footer() {
  return (
    <footer>
      <div className="footer-content">
        <div className="footer-links">
          <a href="/">Home</a>
          <a href="/pets">Pets</a>
          {/* Add more links as needed */}
          <a href="/about">About Us</a>
          <a href="/contact">Contact Us</a>
        </div>
        <div className="footer-copyright">
          &copy; {new Date().getFullYear()} Pet Adoption App
        </div>
      </div>
    </footer>
  );
}

export default Footer;
