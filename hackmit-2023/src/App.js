import './App.css';
import Nav from './Nav.js';
import Message from './Message.js';
import Stats from './Stats.js';

function App() {
  return (
    <div className="site-container">
      <Nav />
      <div className="content-container">
        <Message message="You are sad"/>
        <Stats />
      </div>
    </div>
  );
}

export default App;
