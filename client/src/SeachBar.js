import React, { useState, useEffect } from 'react';

function SearchBar({ onSearch }) {
  const [location, setLocation] = useState('');
  const [priceRange, setPriceRange] = useState('');

  useEffect(() => {
    // This effect will be called whenever location or priceRange changes
    // You can perform search functionality here, like calling an API endpoint
    // For demonstration purposes, I'm just logging the search parameters
    console.log('Location:', location);
    console.log('Price Range:', priceRange);
    
    // Call the onSearch callback with the search parameters
    onSearch({ location, priceRange });

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [location, priceRange]); // Only re-run the effect if these values change

  const handleLocationChange = (e) => {
    setLocation(e.target.value);
  };

  const handlePriceRangeChange = (e) => {
    setPriceRange(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // This prevents the form from triggering a full page reload
    // You can add additional validation or logic here before calling onSearch
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

