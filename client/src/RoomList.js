import React from 'react';

function RoomList({ rooms }) {
  return (
    <div>
      <h2>Search Results</h2>
      <ul>
        {rooms.map(room => (
          <li key={room.id}>
            <h3>{room.name}</h3>
            <p>Description: {room.description}</p>
            <p>Price: {room.price}</p>
            {/* Add more room details here */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RoomList;

