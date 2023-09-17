import React, { useEffect, useState } from 'react';
import './App.css';
import Nav from './Nav.js';
import Message from './Message.js';
import Stats from './Stats.js';

import messages from './messages.json'

const CategoryContext = React.createContext({
  category: 0, fetchCategory: () => {}
})

function App() {
  const [category, setCategory] = useState([])
  const fetchCategory = async () => {
    const response = await fetch("http://localhost:8000/mood-message/")
    const category = await response.json()
    setCategory(category.closest_match)
  }
  useEffect(() => {
    fetchCategory()
  }, [])

  const messageId = category;
  const message = messages.find(item => item.id === messageId).message;
  const color = messages.find(item => item.id === messageId).color;

  return (
    <CategoryContext.Provider value={{category, fetchCategory}}>
      <div className="site-container" style={{backgroundColor: color}}>
        <Nav />
        <div className="content-container">
          <Message message={message} />
          <Stats />
        </div>
      </div>
    </CategoryContext.Provider>

    
  );
}

export default App;
