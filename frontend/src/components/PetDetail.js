import React, { useEffect, useState } from 'react';

function PetDetail(props) {
  const [pet, setPet] = useState(null);

  // Simulate fetching pet data based on the ID from the route parameters
  useEffect(() => {
    const { match } = props;
    const petId = match.params.id;

    // You can replace this with an actual API request to fetch pet data
    // Example fetch request:
    // fetch(`/api/pets/${petId}`)
    //   .then(response => response.json())
    //   .then(data => setPet(data))
    //   .catch(error => console.error('Error fetching pet data:', error));

    // Simulated pet data (replace with actual data)
    const simulatedPetData = {
      id: petId,
      name: 'Fluffy',
      type: 'Cat',
      breed: 'Persian',
      age: 4,
      description: 'A lovely Persian cat with fluffy fur.',
    };

    setPet(simulatedPetData);
  }, [props]);

  if (!pet) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{pet.name}</h2>
      <p>Type: {pet.type}</p>
      <p>Breed: {pet.breed}</p>
      <p>Age: {pet.age} years</p>
      <p>Description: {pet.description}</p>
      
      {/* Add additional details and components as needed */}
    </div>
  );
}

export default PetDetail;
