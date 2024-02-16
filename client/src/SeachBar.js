import React, { useState } from 'react';

function SearchBar({ onSearch }) {
  const [location, setLocation] = useState('');
  const [priceRange, setPriceRange] = useState('');

  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  const handlePriceRangeChange = (e) => {
    setPriceRange(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({ location, priceRange });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Location"
        value={location}
        onChange={handleLocationChange}
      />
      <input
        type="text"
        placeholder="Price Range"
        value={priceRange}
        onChange={handlePriceRangeChange}
      />
      <button type="submit">Search</button>
    </form>
  );
}

export default SearchBar;
