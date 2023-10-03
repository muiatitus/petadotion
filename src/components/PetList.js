// PetList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function PetList() {
  const [pets, setPets] = useState([]);

  useEffect(() => {
    axios.get('/api/pets')
      .then((response) => {
        setPets(response.data);
      })
      .catch((error) => {
        console.error('Error fetching pets:', error);
      });
  }, []);

  return (
    <div>
      {pets.map((pet) => (
        <div key={pet.id}>
          <h2>{pet.name}</h2>
          <p>{pet.description}</p>
          {/* Display more pet details */}
        </div>
      ))}
    </div>
  );
}

export default PetList;
