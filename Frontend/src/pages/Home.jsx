// import React from 'react'
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">Clustering Application</h1>
      <div className="space-y-4">
        <Link to="/Kmedoid">
          <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition">
            Go to K-Medoid
          </button>
        </Link>
        <Link to="/Kmean">
          <button className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 transition">
            Go to K-Mean
          </button>
        </Link>
      </div>
    </div>
  );
};

export default Home;
