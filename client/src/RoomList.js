import React from 'react';

function RoomList({ rooms }) {
  return (
    <div>
      <h2>Room List</h2>
      <ul>
        {rooms.map(room => (
          <li key={room.id}>
            {room.name} - {room.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RoomList;
