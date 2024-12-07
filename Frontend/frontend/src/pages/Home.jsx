import axios from 'axios';
import React, { useEffect, useState } from 'react';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5001/cluster');
        console.log('API Response:', response.data); // Debug log
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  // Filter data berdasarkan cluster
  const cluster0 = data.filter((item) => item.cluster === 0);
  const cluster1 = data.filter((item) => item.cluster === 1);
  const cluster2 = data.filter((item) => item.cluster === 2);

  // Reusable Table Component
  const Table = ({ title, data }) => (
    <div className="mb-8">
      <h2 className="text-xl font-semibold text-center mb-4">{title}</h2>
      <div className="overflow-x-auto">
        <table className="table-auto border-collapse border border-gray-300 w-full">
          <thead className="bg-gray-200">
            <tr>
              <th className="border border-gray-300 px-4 py-2">No</th>
              <th className="border border-gray-300 px-4 py-2">Nama Mahasiswa</th>
              <th className="border border-gray-300 px-4 py-2">Jurusan</th>
              <th className="border border-gray-300 px-4 py-2">IPK</th>
              <th className="border border-gray-300 px-4 py-2">Cluster</th>
              <th className="border border-gray-300 px-4 py-2">Nilai Prediksi</th>
              <th className="border border-gray-300 px-4 py-2">Nilai Selisih</th>
              <th className="border border-gray-300 px-4 py-2">MAPE</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr
                key={index}
                className={`${
                  index % 2 === 0 ? 'bg-gray-100' : 'bg-white'
                } hover:bg-blue-100`}
              >
                <td className="border border-gray-300 px-4 py-2 text-center">{item.no}</td>
                <td className="border border-gray-300 px-4 py-2">{item.nama_mahasiwa}</td>
                <td className="border border-gray-300 px-4 py-2">{item.jurusan}</td>
                <td className="border border-gray-300 px-4 py-2 text-center">{item.ipk}</td>
                <td className="border border-gray-300 px-4 py-2 text-center">{item.cluster}</td>
                <td className="border border-gray-300 px-4 py-2 text-center">{item.nilai_prediksi.toFixed(6)}</td>
                <td className="border border-gray-300 px-4 py-2 text-center">{item.nilai_selisih.toFixed(6)}</td>
                <td className="border border-gray-300 px-4 py-2 text-center">
                  {item.mape.toFixed(5)}%
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-center mb-6">Hasil Clustering Mahasiswa</h1>
      {/* Tabel Cluster 1 */}
      <Table title="Cluster 0" data={cluster0} />

      {/* Tabel Cluster 2 */}
      <Table title="Cluster 1" data={cluster1} />

      {/* Tabel Cluster 3 */}
      <Table title="Cluster 2" data={cluster2} />
    </div>
  );
};

export default App;
