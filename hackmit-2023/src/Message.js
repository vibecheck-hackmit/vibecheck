import React from 'react';
import './App.css';

function Message(props) {
  return (
    <div className="message-container" id="message">
      <h1>{props.message}</h1>
    </div>
  )
}

export default Message;