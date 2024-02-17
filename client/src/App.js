import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/search" element={<SearchResults />} />
        <Route path="/room/:id" element={<RoomDetails />} />
        <Route path="/booking/:id" element={<Booking />} />
      </Routes>
    </Router>
  );
}
export default App;