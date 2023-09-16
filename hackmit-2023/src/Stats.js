import React from 'react';
import './App.css';

import List from './List.js';
import BarChart from './BarChart.js';
import data from './sample.json';

function Stats() {
  return (
    <div>
      <h2>Statistics</h2>
      <div className="stats-container">
        <List data={data} title="Top Tracks" category="track_name"/>
        <List data={data} title="Top Artists" category="artist_name"/>
        <BarChart data={data}/>
      </div>
    </div>
  )
}

export default Stats;