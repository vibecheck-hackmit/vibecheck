import React from 'react';
import Fade from 'react-reveal/Fade';
import './App.css';

function Message(props) {
  return (
    <Fade big cascade>
      <div className="message-container" id="message">
        <h2>Vibe: {props.mood}</h2>
        <h1>{props.message}</h1>
      </div>
    </Fade>
  )
}

export default Message;