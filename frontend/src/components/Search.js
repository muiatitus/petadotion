import React, { useState } from 'react';

function Search() {
  const [searchQuery, setSearchQuery] = useState('');

  const handleInputChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSearch = (event) => {
    event.preventDefault();
    // TODO: Implement search logic here
    console.log('Search query:', searchQuery);
    // You can add your search functionality here, e.g., making an API request
  };

  return (
    <div>
      <h2>Search for Pets</h2>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          placeholder="Search by name, type, or breed"
          value={searchQuery}
          onChange={handleInputChange}
        />
        <button type="submit">Search</button>
      </form>
    </div>
  );
}

export default Search;
