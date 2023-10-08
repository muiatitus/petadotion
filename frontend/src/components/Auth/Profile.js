import React, { useState, useEffect } from 'react';
import axios from 'axios';

const containerStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  maxWidth: '400px',
  margin: '0 auto',
};

const formStyle = {
  width: '100%',
};

const inputStyle = {
  marginBottom: '15px',
  padding: '10px',
  width: '100%',
  borderRadius: '5px',
  border: '1px solid #ccc',
};

const buttonStyle = {
  backgroundColor: '#007BFF',
  color: 'white',
  padding: '10px 20px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  marginRight: '10px',
};

function Profile() {
  const [userData, setUserData] = useState({
    username: '',
    email: '',
  });
  const [isEditing, setIsEditing] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Simulate user data retrieval (e.g., from an API)
  useEffect(() => {
    // TODO: Replace with actual API request to fetch user data
    const fetchUserData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/user'); // Replace with your user data API endpoint
        const data = response.data;
        setUserData(data);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching user data:', error);
        setError('Error fetching user data. Please try again.');
        setIsLoading(false);
      }
    };

    fetchUserData();
  }, []);

  const handleEditClick = () => {
    setIsEditing(true);
  };

  const handleSaveClick = async () => {
    try {
      // Make an HTTP PUT request to update the user's profile
      await axios.put('http://localhost:5000/profile/edit', userData); // Replace with your update profile API endpoint
      setIsEditing(false);
      alert('Profile updated successfully');
    } catch (error) {
      console.error('Error updating profile:', error);
      alert('Profile update failed. Please try again.');
    }
  };

  const handleCancelClick = () => {
    setIsEditing(false);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setUserData({
      ...userData,
      [name]: value,
    });
  };

  return (
    <div style={containerStyle}>
      <h2>User Profile</h2>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <div>
          {error ? (
            <p>Error: {error}</p>
          ) : (
            <>
              {isEditing ? (
                <div style={formStyle}>
                  <label htmlFor="username">Username:</label>
                  <input
                    type="text"
                    id="username"
                    name="username"
                    value={userData.username}
                    onChange={handleInputChange}
                    required
                    style={inputStyle}
                  />
                  <br />

                  <label htmlFor="email">Email:</label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={userData.email}
                    onChange={handleInputChange}
                    required
                    style={inputStyle}
                  />
                  <br />

                  <button onClick={handleSaveClick} style={buttonStyle}>Save</button>
                  <button onClick={handleCancelClick} style={buttonStyle}>Cancel</button>
                </div>
              ) : (
                <div>
                  <p><strong>Username:</strong> {userData.username}</p>
                  <p><strong>Email:</strong> {userData.email}</p>
                  <button onClick={handleEditClick} style={buttonStyle}>Edit Profile</button>
                </div>
              )}
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default Profile;
