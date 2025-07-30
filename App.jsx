import React from 'react';
import Employees from './Employees.jsx';
import Columns from './Columns.jsx'; // 1. Import the new Columns component

function App() {
  return (
    <div className="App">
      {/* This is your existing Employees table */}
      <Employees />

      {/* This is a simple horizontal line to separate the sections */}
      <hr className="my-8 border-t border-gray-300" />

      {/* 2. This renders your new Columns component on the page */}
      <Columns />
    </div>
  );
}

export default App;
