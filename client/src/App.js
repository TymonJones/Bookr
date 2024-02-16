import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/search" component={SearchResults} />
        <Route path="/room/:id" component={RoomDetails} />
        <Route path="/booking/:id" component={Booking} />
      </Switch>
    </Router>
  );
};