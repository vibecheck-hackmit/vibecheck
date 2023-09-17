import React, { useEffect, useState } from 'react';
import './App.css';
import Nav from './Nav.js';
import Message from './Message.js';
import Stats from './Stats.js';

import messages from './messages.json'

const CategoryContext = React.createContext({
  category: 0, fetchCategory: () => {}
})

let cat = 0;

async function test() {
  let response = await fetch("http://localhost:8000/mood-message/");
  let category = await response.json();
  cat = category.closest_match;
  console.log(category.closest_match);
}

await test();

function App() {
  // const [category, setCategory] = useState([])
  // const fetchCategory = async () => {
  //   const response = await fetch("http://localhost:8000/mood-message/")
  //   const category = await response.json()
  //   setCategory(category)
  // }
  // useEffect(() => {
  //   fetchCategory()
  // }, [])
  
  // console.log(category);

  // const vibeMessage = messages.find(item => item.id === 2).message;
  // const vibeMood = messages.find(item => item.id === 2).mood;
  // const vibeColor = messages.find(item => item.id === 2).color;
  const vibeMessage = messages.find(item => item.id === cat).message;
  const vibeMood = messages.find(item => item.id === cat).mood;
  const vibeColor = messages.find(item => item.id === cat).color;

  return (
    // <CategoryContext.Provider value={{category, fetchCategory}}>
      <div className="site-container" style={{backgroundColor: vibeColor}}>
        <Nav />
        <div className="content-container">
          <Message message={vibeMessage} mood={vibeMood} />
          <Stats />
        </div>
      </div>
    // </CategoryContext.Provider>
  );
}

export default App;
