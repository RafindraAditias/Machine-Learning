import pandas as pd
from sklearn.cluster import KMeans

# Load data dari CSV
data = pd.read_csv('dataMahasiswa.csv')

# Menampilkan data awal
print(data)

# Ambil kolom IPK sebagai fitur untuk clustering
X = data[['ipk']]

# Inisialisasi KMeans dengan 3 cluster
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit model dan prediksi cluster
data['cluster'] = kmeans.fit_predict(X)

# Centroid dari masing-masing cluster
centroids = kmeans.cluster_centers_.flatten()

# Nilai Prediksi (nilai centroid dari cluster)
data['nilai_prediksi'] = data['cluster'].apply(lambda x: centroids[x])

# Nilai Selisih (ipk - nilai_prediksi)
data['nilai_selisih'] = data['ipk'] - data['nilai_prediksi']

# MAPE (Mean Absolute Percentage Error)
data['mape'] = abs(data['nilai_selisih']) / data['ipk'] * 100

# Menampilkan hasil akhir
print(data[['no', 'nama_mahasiwa', 'jurusan', 'ipk', 'cluster', 'nilai_prediksi', 'nilai_selisih', 'mape']])
