import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Hero from "../components/shared/hero";

const Home = () => {
  const [kMeanImage, setKMeanImage] = useState(null);
  const [kMeanImage1, setKMeanImage1] = useState(null);
  const [kMeanImage1K, setKMeanImage1K] = useState(null);
  const [kMeanImage2, setKMeanImage2] = useState(null);
  const [kMeanImage2K, setKMeanImage2K] = useState(null);
  const [kMeanImage3K, setKMeanImage3K] = useState(null);

  const [kMeanImage1M, setKMeanImage1M] = useState(null);
  const [kMeanImage2M, setKMeanImage2M] = useState(null);
  const [kMedoidImage, setKMedoidImage] = useState(null);

  // Fungsi utilitas untuk mengambil gambar dari backend
  const fetchImage = async (endpoint, setImage) => {
    try {
      const timestamp = new Date().getTime(); // Unique timestamp to avoid caching
      const response = await axios.get(`${endpoint}?timestamp=${timestamp}`, {
        responseType: "blob",
      });
      const url = URL.createObjectURL(response.data);
      setImage(url);
    } catch (error) {
      console.error(`Error fetching image from ${endpoint}:`, error);
    }
  };

  // Mengambil semua gambar saat komponen dimount
  useEffect(() => {
    fetchImage("http://127.0.0.1:5001/Kmean/visualize1", setKMeanImage1);
    fetchImage("http://127.0.0.1:5001/Kmean/visualize1K", setKMeanImage1K);
    fetchImage("http://127.0.0.1:5001/Kmean/visualize2", setKMeanImage2);
    fetchImage("http://127.0.0.1:5001/Kmean/visualize2K", setKMeanImage2K);
    fetchImage("http://127.0.0.1:5001/Kmean/visualize3", setKMeanImage);
    fetchImage("http://127.0.0.1:5001/Kmean/visualize3K", setKMeanImage3K);
    
    fetchImage("http://127.0.0.1:5001/Kmedoid/visualize", setKMedoidImage);
    fetchImage("http://127.0.0.1:5001/Kmedoid/visualize1M", setKMeanImage1M);
    fetchImage("http://127.0.0.1:5001/Kmedoid/visualize2M", setKMeanImage2M);
  }, []);

  return (
    <div className="text-black">
      <Hero />
      <h1 className="text-3xl font-bold mb-4 text-center">
        Clustering Application
      </h1>

      {/* Bagian Visualisasi */}
      <div className="items-center justify-around p-10">
        {/* Visualisasi K-Means */}
        <div className="flex flex-col items-center">
          <div className="flex gap-10">
            <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
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
                <p>Loading K-Means visualization ITERASI 1</p>
              )}
            </div>
            {/* Visualisasi K-Means Iterasi 2 */}
            <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
              <h2 className="text-2xl font-semibold mb-4">
                K-Means Visualization ITERASI 2
              </h2>
              {kMeanImage2 ? (
                <img
                  src={kMeanImage2}
                  alt="K-Means Visualization ITERASI 2"
                  className="w-full h-auto rounded"
                />
              ) : (
                <p>Loading K-Means visualization ITERASI 2</p>
              )}
            </div>
          </div>

          {/* Visualisasi K-Means Kedekatan */}
          <div className="flex gap-10">
            KEDEKATAN 1
            <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
              <h2 className="text-2xl font-semibold mb-4">
                K-Means Visualization Kedekatan Iterasi 1
              </h2>
              {kMeanImage1K ? (
                <img
                  src={kMeanImage1K}
                  alt="K-Means Visualization Kedekatan"
                  className="w-full h-auto rounded"
                />
              ) : (
                <p>Loading K-Means visualization Kedekatan...</p>
              )}
            </div>
            {/* Visualisasi K-Means Kedekatan */}
            <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
              <h2 className="text-2xl font-semibold mb-4">
                K-MEDOID Visualization Kedekatan 1
              </h2>
              {kMeanImage1M ? (
                <img
                  src={kMeanImage1M}
                  alt="K-Means Visualization Kedekatan"
                  className="w-full h-auto rounded"
                />
              ) : (
                <p>Loading K-Means visualization Kedekatan...</p>
              )}
            </div>
          </div>

          <div className="flex gap-10">
            kedekatin 2{/* Visualisasi MAPE KMEAN KMEDOID */}
            <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
              <h2 className="text-2xl font-semibold mb-4">
                K-Means Visualization Kedekatan
              </h2>
              {kMeanImage2K ? (
                <img
                  src={kMeanImage2K}
                  alt="K-Means Visualization Kedekatan"
                  className="w-full h-auto rounded"
                />
              ) : (
                <p>Loading K-Means visualization Kedekatan...</p>
              )}
            </div>
            <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
              <h2 className="text-2xl font-semibold mb-4">
                K-MEDOID Visualization Kedekatan
              </h2>
              {kMeanImage2M ? (
                <img
                  src={kMeanImage2M}
                  alt="K-Means Visualization Kedekatan"
                  className="w-full h-auto rounded"
                />
              ) : (
                <p>Loading K-Medoid visualization Kedekatan...</p>
              )}
            </div>
          </div>
        <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
              <h2 className="text-2xl font-semibold mb-4">
                K-Means Visualization Kedekatan
              </h2>
              {kMeanImage3K ? (
                <img
                  src={kMeanImage3K}
                  alt="K-Means Visualization Kedekatan"
                  className="w-full h-auto rounded"
                />
              ) : (
                <p>Loading K-Means visualization Kedekatan...</p>
              )}
            </div>
        <div className="flex gap-10 items-start">
          <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
            <h2 className="text-2xl font-semibold mb-4">
              K-Means MAPE Visualization
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

          <div className="w-full max-w-3xl shadow-md rounded bg-gray-400 p-5 mb-6">
            <h2 className="text-2xl font-semibold mb-4">
              K-Medoids MAPE Visualization
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
      </div>
      {/* Visualisasi K-Means Iterasi 1 */}

      {/* Tombol Navigasi */}
      <div className="flex flex-col items-center justify-center mt-10">
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
    </div>
  );
};

export default Home;
