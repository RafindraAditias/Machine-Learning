import React, { useState } from 'react';

const DataUploadForm = () => {
  const [no, setNo] = useState('');
  const [jurusan, setJurusan] = useState('');
  const [namaMahasiswa, setNamaMahasiswa] = useState('');
  const [ipk, setIpk] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('no', no);
    formData.append('jurusan', jurusan);
    formData.append('nama_mahasiswa', namaMahasiswa);
    formData.append('ipk', ipk);

    try {
      const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
      });
      const result = await response.json();
      if (response.ok) {
        alert('Data uploaded successfully!');
        console.log(result);
      } else {
        alert('Error uploading data!');
        console.log(result);
      }
    } catch (error) {
      alert('Error with the request');
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Upload Data to CSV</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>No:</label>
          <input
            type="text"
            value={no}
            onChange={(e) => setNo(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Jurusan:</label>
          <input
            type="text"
            value={jurusan}
            onChange={(e) => setJurusan(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Nama Mahasiswa:</label>
          <input
            type="text"
            value={namaMahasiswa}
            onChange={(e) => setNamaMahasiswa(e.target.value)}
            required
          />
        </div>
        <div>
          <label>IPK:</label>
          <input
            type="text"
            value={ipk}
            onChange={(e) => setIpk(e.target.value)}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default DataUploadForm;
