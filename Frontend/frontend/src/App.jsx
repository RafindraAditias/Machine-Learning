import React from 'react';
import { Route, Routes } from 'react-router-dom';
import InputData from './pages/InputData';
import Home from './pages/Home';

const App = () => {
  return (
    <div className="app">
      <Routes>
        <Route path="/Home" element={<Home />} />
        <Route path="/Form" element={<InputData />} />
      </Routes>
    </div>
  );
};

export default App;
