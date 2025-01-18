const hero = () => {
  return (
    <div className="bg-[#1d4c44] flex p-10 items-center justify-between pb-20 mb-10">
      <div className="">
        <h1 className="text-5xl font-bold mb-4 text-white">
          Penelitian
          <br />
          <span className="text-[#c3930c] font-quicksand">K-Medoids dan K-Means</span> <br />
          Clustering
        </h1>
        <p className="text-lg mb-6 text-white w-[70%]">
          Penelitian ini berfokus pada penerapan metode K-Medoids dan K-Means
          untuk pengelompokan data mahasiswa berdasarkan Indeks Prestasi
          Kumulatif (IPK). Metode ini membantu dalam memahami pola dan
          pengelompokan mahasiswa secara lebih efektif.
        </p>
      </div>
      <img src="../../public/image/networking.png" alt="" />
    </div>
  );
};

export default hero;
