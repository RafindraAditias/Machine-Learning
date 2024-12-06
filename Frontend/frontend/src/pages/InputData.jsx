import React, { useState } from "react";

const InputData = () => {
  const [no, setNo] = useState("");
  const [jurusan, setJurusan] = useState("");
  const [namaMahasiswa, setNamaMahasiswa] = useState("");
  const [ipk, setIpk] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = { no, jurusan, namaMahasiswa, ipk };

    try {
      const response = await fetch("http://127.0.0.1:5000/data", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        alert("Data uploaded successfully!");
      } else {
        alert("Error uploading data!");
      }
    } catch (error) {
      alert("Error with the request");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form
        className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
        onSubmit={handleSubmit}
      >
        <h2 className="text-2xl font-bold mb-6 text-center">
          Input Data Mahasiswa
        </h2>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            No
          </label>
          <input
            type="text"
            value={no}
            onChange={(e) => setNo(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Jurusan
          </label>
          <input
            type="text"
            value={jurusan}
            onChange={(e) => setJurusan(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Nama Mahasiswa
          </label>
          <input
            type="text"
            value={namaMahasiswa}
            onChange={(e) => setNamaMahasiswa(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            IPK
          </label>
          <input
            type="text"
            value={ipk}
            onChange={(e) => setIpk(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            required
          />
        </div>
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default InputData;
