import React from 'react';
import './App.css';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip
);

export const options = {
  indexAxis: 'y',
  responsive: true,
};

const labels = ['Danceability', 'Energy', 'Valence'];
export const data = {
  labels,
  datasets: [{
      data: labels.map(() => 100),
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
  ],
};

function BarChart(props) {
  return (
    <div>
      <h3>Characteristics</h3>
      <Bar options={options} data={data} className="barChart"/>;
    </div>
  )
}

export default BarChart;


