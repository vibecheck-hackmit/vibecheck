import React, { useEffect, useState } from 'react';
import './App.css';
import Nav from './Nav.js';
import Message from './Message.js';
import Stats from './Stats.js';

import messages from './messages.json'


function App() {
  const [categorizeResult, setCategorizeResult] = useState(null);

useEffect(() => {
  fetch('../stats.py/categorize', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({}),
  })
    .then((response) => response.json())
    .then((data) => {
      const categorizeResult = data.result;
      console.log('Categorize Result:', categorizeResult);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  })
    .then((response) => response.json())
    .then((data) => {
      const result = data.result;
      setCategorizeResult(result);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
// }, []);



  const messageId = {categorizeResult};
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
