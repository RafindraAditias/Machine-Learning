# import numpy as np
# import pandas as pd

# # Load data from CSV
# data = pd.read_csv('dataMahasiswa.csv')

# # Tampilkan data
# print(data)
# # Centroid yang Diperbarui (ITERASI 3)
# centroids = [3.01, 3.45, 3.79]

# # Menentukan cluster berdasarkan kedekatan IPK dengan centroid
# def assign_cluster(ipk, centroids):
#     distances = [abs(ipk - centroid) for centroid in centroids]
#     return np.argmin(distances)

# df['cluster'] = df['ipk'].apply(assign_cluster, centroids=centroids)

# # Nilai Prediksi (nilai centroid dari cluster)
# df['nilai_prediksi'] = df['cluster'].apply(lambda x: centroids[x])

# # Nilai Selisih (ipk - nilai_prediksi)
# df['nilai_selisih'] = df['ipk'] - df['nilai_prediksi']

# # MAPE (Mean Absolute Percentage Error)
# df['mape'] = abs(df['nilai_selisih']) / df['ipk'] * 100

# # Menampilkan hasil akhir
# print(df[['no', 'nama_mahasiwa', 'jurusan', 'ipk', 'cluster', 'nilai_prediksi', 'nilai_selisih', 'mape']])

# import pandas as pd
# from sklearn.cluster import KMeans

# # Load data dari CSV
# data = pd.read_csv('dataMahasiswa.csv')

# # Pastikan kolom IPK ada di dataset
# if 'ipk' not in data.columns:
#     raise ValueError("Kolom 'ipk' tidak ditemukan di data.")

# # Inisialisasi KMeans
# kmeans = KMeans(n_clusters=3, random_state=42)

# # Latih model KMeans
# ipk_values = data['ipk'].values.reshape(-1, 1)  # Konversi ke 2D array
# kmeans.fit(ipk_values)

# # Dapatkan cluster dan centroids
# data['cluster'] = kmeans.labels_
# centroids = kmeans.cluster_centers_.flatten()

# # Hitung nilai prediksi berdasarkan centroid cluster
# data['nilai_prediksi'] = data['cluster'].apply(lambda x: centroids[x])

# # Hitung nilai selisih dan MAPE
# data['nilai_selisih'] = data['ipk'] - data['nilai_prediksi']
# data['mape'] = abs(data['nilai_selisih']) / data['ipk'] * 100

# # Tampilkan hasil akhir
# print(data[['no', 'nama_mahasiwa', 'jurusan', 'ipk', 'cluster', 'nilai_prediksi', 'nilai_selisih', 'mape']])

from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans

app = Flask(__name__)
CORS(app)  # Tambahkan ini untuk mengizinkan semua permintaan CORS

@app.route('/cluster', methods=['GET'])
def cluster():
    data = pd.read_csv('dataMahasiswa.csv')
    kmeans = KMeans(n_clusters=3, random_state=42)
    ipk_values = data['ipk'].values.reshape(-1, 1)
    kmeans.fit(ipk_values)

    data['cluster'] = kmeans.labels_
    centroids = kmeans.cluster_centers_.flatten()
    data['nilai_prediksi'] = data['cluster'].apply(lambda x: centroids[x])
    data['nilai_selisih'] = data['ipk'] - data['nilai_prediksi']
    data['mape'] = abs(data['nilai_selisih']) / data['ipk'] * 100

    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

