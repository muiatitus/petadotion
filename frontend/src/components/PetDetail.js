// PetDetail.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function PetDetail() {
  const { id } = useParams();
  const [pet, setPet] = useState(null);

  useEffect(() => {
    axios.get(`/api/pets/${id}`)
      .then((response) => {
        setPet(response.data);
      })
      .catch((error) => {
        console.error('Error fetching pet details:', error);
      });
  }, [id]);

  if (!pet) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{pet.name}</h2>
      <p>{pet.description}</p>
      {/* Display more pet details */}
    </div>
  );
}

export default PetDetail;
