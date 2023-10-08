import React, { useEffect, useState } from 'react';
import axios from 'axios';

function PetList() {
  const [pets, setPets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [category, setCategory] = useState('');

  useEffect(() => {
    // Make an HTTP GET request to fetch the list of available pets from your server
    axios.get('http://localhost:5000/pets') // Replace with your server's URL
      .then((response) => {
        setPets(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching pet data:', error);
        setLoading(false);
      });
  }, []);

  const filteredPets = pets
    .filter(pet =>
      pet.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
      (category === '' || pet.type.toLowerCase() === category.toLowerCase())
    );

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Available Pets for Adoption</h2>
      <div>
        <input
          type="text"
          placeholder="Search by name"
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
        />
        <select
          value={category}
          onChange={e => setCategory(e.target.value)}
        >
          <option value="">All Categories</option>
          <option value="cat">Cat</option>
          <option value="dog">Dog</option>
          {/* Add more category options as needed */}
        </select>
      </div>
      <ul>
        {filteredPets.map(pet => (
          <li key={pet.id}>
            <h3>{pet.name}</h3>
            <p>Type: {pet.type}</p>
            <p>Breed: {pet.breed}</p>
            <p>Age: {pet.age} years</p>
            <p>{pet.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PetList;
