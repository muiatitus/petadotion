// Home.js

import React from 'react';

const containerStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  maxWidth: '400px',
  margin: '0 auto',
  textAlign: 'center',
};

const headerStyle = {
  fontSize: '24px',
  marginBottom: '15px',
};

const paragraphStyle = {
  fontSize: '16px',
};

function Home({ authenticated }) {
  return (
    <div style={containerStyle}>
      <h2 style={headerStyle}>Welcome to the Pet Adoption App</h2>
      {authenticated && <p>Welcome, {localStorage.getItem('username')}!</p>}
      <p style={paragraphStyle}>Find your new furry friend today!</p>

      {/* Add content and components specific to your home page */}
    </div>
  );
}

export default Home;
