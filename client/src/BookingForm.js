import React, { useState } from 'react';

function BookingForm({ onSubmit }) {
  const [dates, setDates] = useState('');
  // Add more booking form fields as needed

  const handleDatesChange = (e) => {
    setDates(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ dates });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Dates"
        value={dates}
        onChange={handleDatesChange}
      />
      {/* Add more input fields for booking form */}
      <button type="submit">Book Now</button>
    </form>
  );
}

export default BookingForm;
