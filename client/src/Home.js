
import React from 'react';
import { useHistory } from 'react-router-dom';
import SearchBar from './SearchBar';

function Home() {
  const history = useHistory();

  const handleSearch = (searchParams) => {
    // Redirect to the search results page with the search parameters in the URL query string
    history.push(`/search?location=${searchParams.location}&priceRange=${searchParams.priceRange}`);
  };

  return (
    <div>
      <h1>Welcome to Room Booking App</h1>
      <SearchBar onSearch={handleSearch} />
    </div>
  );
}

export default Home;
