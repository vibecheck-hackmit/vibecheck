import './App.css';
import Nav from './Nav.js';
import Message from './Message.js';
import Stats from './Stats.js';

import messages from './messages.json'



function App() {
  const messageId = 6;
  const message = messages.find(item => item.id === messageId).message;
  const color = messages.find(item => item.id === messageId).color;

  return (
    <div className="site-container" style={{backgroundColor: color}}>
      <Nav />
      <div className="content-container">
        <Message message={message} />
        <Stats />
      </div>
    </div>
  );
}

export default App;
