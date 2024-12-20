// import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Kmean from './pages/Kmean';
import Kmedoid from './pages/Kmedoid';

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Kmean" element={<Kmean />} />
        <Route path="/Kmedoid" element={<Kmedoid />} />
      </Routes>
    </div>
  );
};

export default App;
