import numpy as np
import pandas as pd

# Load data from CSV
data = pd.read_csv('dataMahasiswa.csv')

# Tampilkan data
print(data)
# Centroid yang Diperbarui (ITERASI 3)
centroids = [3.01, 3.45, 3.79]

# Menentukan cluster berdasarkan kedekatan IPK dengan centroid
def assign_cluster(ipk, centroids):
    distances = [abs(ipk - centroid) for centroid in centroids]
    return np.argmin(distances)

df['cluster'] = df['ipk'].apply(assign_cluster, centroids=centroids)

# Nilai Prediksi (nilai centroid dari cluster)
df['nilai_prediksi'] = df['cluster'].apply(lambda x: centroids[x])

# Nilai Selisih (ipk - nilai_prediksi)
df['nilai_selisih'] = df['ipk'] - df['nilai_prediksi']

# MAPE (Mean Absolute Percentage Error)
df['mape'] = abs(df['nilai_selisih']) / df['ipk'] * 100

# Menampilkan hasil akhir
print(df[['no', 'nama_mahasiwa', 'jurusan', 'ipk', 'cluster', 'nilai_prediksi', 'nilai_selisih', 'mape']])
