import React from 'react';
import Fade from 'react-reveal/Fade';
import './App.css';

import List from './List.js';
import BarChart from './BarChart.js';
import data from './sample.json';

function Stats() {
  return (
    <Fade cascade>
      <h2>Statistics</h2>
      <div className="stats-container">
        <Fade>
          <List data={data} title="Top Tracks" category="track_name"/>
          <List data={data} title="Top Artists" category="artist_name"/>
          <BarChart data={data}/>
        </Fade>
      </div>
    </Fade>
  )
}

export default Stats;