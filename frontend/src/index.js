import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Import your global CSS styles here
import App from './App'; // Import your main application component (e.g., App.js)
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
