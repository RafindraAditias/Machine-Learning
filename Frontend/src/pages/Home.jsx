import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Hero from "../components/shared/hero";

const Home = () => {
  const [kMeanImage, setKMeanImage] = useState(null);
  const [kMeanImage1, setKMeanImage1] = useState(null);
  const [kMeanImage2, setKMeanImage2] = useState(null);
  const [kMedoidImage, setKMedoidImage] = useState(null);

  useEffect(() => {
    const timestamp = new Date().getTime(); // Unique timestamp to avoid caching

    axios
      .get(`http://127.0.0.1:5001/Kmean/visualize3?timestamp=${timestamp}`, {
        responseType: "blob",
      })
      .then((response) => {
        const url = URL.createObjectURL(response.data);
        setKMeanImage(url);
      })
      .catch((error) =>
        console.error("Error fetching K-Means visualization:", error)
      );

    axios
      .get(`http://127.0.0.1:5001/Kmean/visualize1?timestamp=${timestamp}`, {
        responseType: "blob",
      })
      .then((response) => {
        const url = URL.createObjectURL(response.data);
        setKMeanImage1(url);
      })
      .catch((error) =>
        console.error("Error fetching K-Means visualization ITERASI 1:", error)
      );

    axios
      .get(`http://127.0.0.1:5001/Kmean/visualize2?timestamp=${timestamp}`, {
        responseType: "blob",
      })
      .then((response) => {
        const url = URL.createObjectURL(response.data);
        setKMeanImage2(url);
      })
      .catch((error) =>
        console.error("Error fetching K-Means visualization ITERASI 1:", error)
      );

    axios
      .get(`http://127.0.0.1:5001/Kmedoid/visualize2?timestamp=${timestamp}`, {
        responseType: "blob",
      })
      .then((response) => {
        const url = URL.createObjectURL(response.data);
        setKMedoidImage(url);
      })
      .catch((error) =>
        console.error("Error fetching K-Medoids visualization:", error)
      );
  }, []);

  return (
    <div className="text-black">
      <Hero />
      <h1 className="text-3xl font-bold mb-4 text-center">
        Clustering Application
      </h1>
      <div className="flex items-center justify-around">
        <div className="items-center justify-center p-6 space-y-7 ">
          <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5">
            <h2 className="text-2xl font-semibold mb-4">
              K-Means Visualization
            </h2>
            {kMeanImage ? (
              <img
                src={kMeanImage}
                alt="K-Means Visualization"
                className="w-full h-auto rounded"
              />
            ) : (
              <p>Loading K-Means visualization...</p>
            )}
          </div>

          <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5">
            <h2 className="text-2xl font-semibold mb-4">
              K-Means Visualization ITERASI 1
            </h2>
            {kMeanImage1 ? (
              <img
                src={kMeanImage1}
                alt="K-Means Visualization ITERASI 1"
                className="w-full h-auto rounded"
              />
            ) : (
              <p>Loading K-Means visualization ITERASI 1...</p>
            )}
          </div>

          <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5">
            <h2 className="text-2xl font-semibold mb-4">
              K-Means Visualization ITERASI 2
            </h2>
            {kMeanImage2 ? (
              <img
                src={kMeanImage2}
                alt="K-Means Visualization ITERASI 1"
                className="w-full h-auto rounded"
              />
            ) : (
              <p>Loading K-Means visualization ITERASI 2...</p>
            )}
          </div>
        </div>
        <div className="flex items-center justify-center p-6 space-x-7">
          <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5">
            <h2 className="text-2xl font-semibold mb-4">
              K-Medoids Visualization
            </h2>
            {kMedoidImage ? (
              <img
                src={kMedoidImage}
                alt="K-Medoids Visualization"
                className="w-full h-auto rounded"
              />
            ) : (
              <p>Loading K-Medoids visualization...</p>
            )}
          </div>
        </div>
      </div>
      <div className="flex flex-col items-center justify-center">
        <div className="space-y-10">
          <Link to="/Kmedoid">
            <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition m-10">
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
    </div>
  );
};

export default Home;
