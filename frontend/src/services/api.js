import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000'; // Update with your backend API URL

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Define your API methods here
// For example:
export const fetchPets = async () => {
  try {
    const response = await api.get('/pets');
    return response.data;
  } catch (error) {
    console.error('Error fetching pets:', error);
    throw error;
  }
};

export default api;