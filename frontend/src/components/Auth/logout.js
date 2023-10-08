// logout.js

import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';

function Logout() {
  const history = useHistory();

  useEffect(() => {
    // Perform logout logic here, e.g., clear user tokens or cookies
    // Replace this with your actual logout logic

    // After successful logout, redirect to the login page
    history.push('/login');
  }, [history]);

  return <div>Logging out...</div>;
}

export default Logout;
