import React from 'react';
import './App.css';

function List(props) {
  const category = props.category
  return (
    <div>
      <h3>{props.title}</h3>
      {props.data.map((item) => (
        <div>
          <p>{item[category]}</p>
        </div>
      ))}
    </div>
  )
}

export default List;


