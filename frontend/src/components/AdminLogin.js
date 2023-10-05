import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function AdminLogin() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({ email: '', password: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://localhost:5000/admin/login', formData) // Assuming you have a separate login API endpoint for admin
      .then((response) => {
        // Handle successful login
        console.log('Admin login successful:', response.data);
        const { token } = response.data;
        // Save the token to local storage or cookies for future requests

        // Redirect to the admin dashboard
        navigate('/admin/dashboard');
      })
      .catch((error) => {
        // Handle login error
        console.error('Admin login error:', error);
      });
  };

  return (
    <div>
      <h2>Admin Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" name="email" placeholder="Email" onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default AdminLogin;