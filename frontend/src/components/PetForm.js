import React, { useState } from 'react';
import axios from 'axios'; // Import Axios

function PetForm() {
  const [formData, setFormData] = useState({
    name: '',
    type: '',
    breed: '',
    age: '',
    description: '',
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Make an HTTP POST request to add a pet to the database
      await axios.post('http://localhost:5000/pets', formData); // Replace with your server URL

      // Reset the form after successful submission
      setFormData({
        name: '',
        type: '',
        breed: '',
        age: '',
        description: '',
      });

      // Optionally, you can show a success message or navigate to a different page
      console.log('Pet submitted successfully.');
    } catch (error) {
      console.error('Error submitting pet:', error);
    }
  };

  return (
    <div>
      <h2>Add a Pet for Adoption</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="type">Type:</label>
          <input
            type="text"
            id="type"
            name="type"
            value={formData.type}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="breed">Breed:</label>
          <input
            type="text"
            id="breed"
            name="breed"
            value={formData.breed}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="age">Age:</label>
          <input
            type="text"
            id="age"
            name="age"
            value={formData.age}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleInputChange}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default PetForm;
