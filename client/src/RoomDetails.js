import React from 'react';

function RoomDetails({ room }) {
  return (
    <div>
      <h2>{room.name}</h2>
      <p>Description: {room.description}</p>
      <p>Price: {room.price}</p>
      <p>Location: {room.location}</p>
      <p>Amenities: {room.amenities.join(', ')}</p>
      {/* Add more room details here */}
    </div>
  );
}

export default RoomDetails;
