import React from 'react';

function Room({ room }) {
  return (
    <div>
      <h2>{room.name}</h2>
      <p>Description: {room.description}</p>
      <p>Price: {room.price}</p>
      {/* Add more room details here */}
    </div>
  );
}

export default Room;
