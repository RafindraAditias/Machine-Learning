import React from 'react';
import { Route, Routes } from 'react-router-dom';
import InputData from './pages/InputData';

const App = () => {
  return (
    <div className="app">
      <Routes>
        <Route path="/Form" element={<InputData />} />
      </Routes>
    </div>
  );
};

export default App;
