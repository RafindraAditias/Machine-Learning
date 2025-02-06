from flask import Flask, jsonify, send_file
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

# Membaca data dari CSV
data = pd.read_csv('dataMahasiswa.csv')
# KMEAN----------------------------------------------------------------------------------------------
# Endpoint untuk K-Means
@app.route('/Kmean', methods=['GET'])
def cluster_kmeans():
    # Mengambil IPK sebagai input clustering
    ipk_values = data['ipk'].values.reshape(-1, 1)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(ipk_values)

    # Menambahkan hasil clustering ke dalam data
    data['Cluster'] = kmeans.labels_
    centroids = kmeans.cluster_centers_.flatten()
    data['Nilai Prediksi'] = data['Cluster'].apply(lambda x: centroids[x])
    data['Nilai Selisih'] = (data['ipk'] - data['Nilai Prediksi']).round(2)
    data['MAPE'] = (abs(data['Nilai Selisih']) / data['ipk'] * 100).round(2)

    return jsonify(data.to_dict(orient='records'))

# Endpoint untuk visualisasi K-Means ITERASI 1-------------------------------------------------------
data_iterasi1 = pd.read_csv('iterasi1.csv')
@app.route('/Kmean/visualize1', methods=['GET'])
def visualize_kmeans_1():
    # Mengambil IPK sebagai input clustering
    ipk_values = data_iterasi1['ipk'].values.reshape(-1, 1)

    # Nilai centroid awal
    initial_centroids = [[3.11], [3.43], [3.89]]

    # K-Means Clustering dengan centroid awal
    kmeans = KMeans(n_clusters=3, init=np.array(initial_centroids), n_init=1, random_state=42)
    kmeans.fit(ipk_values)
    data_iterasi1['Cluster'] = kmeans.labels_

    # Plot data
    plt.figure(figsize=(8, 6))
    colors = ['red', 'blue', 'green']
    for cluster in range(3):
        cluster_data = data_iterasi1[data_iterasi1['Cluster'] == cluster]
        plt.scatter(cluster_data.index, cluster_data['ipk'], color=colors[cluster], label=f'Cluster {cluster}')
    
    # Centroid plot
    plt.scatter(range(len(kmeans.cluster_centers_)), kmeans.cluster_centers_.flatten(), color='black', marker='X', s=200, label='Centroids')
    plt.title('K-Means Clustering (IPK) ITERASI 1')
    plt.xlabel('Index')
    plt.ylabel('IPK')
    plt.legend()
    plt.grid(True)

    # Simpan gambar dan kirimkan sebagai response
    plt.savefig('kmeans_visualization_iterasi1.png')
    plt.close()
    return send_file('kmeans_visualization_iterasi1.png', mimetype='image/png')

@app.route('/Kmean/visualize1K', methods=['GET'])
def visualize_kedekatan_hasil():
    # Memuat data CSV
    data = pd.read_csv('KmeanIterasi1K.csv')  # Pastikan file CSV ada di folder yang benar

    # Mengecek jumlah data
    print(f"Jumlah data: {len(data)}")
    print(f"Jumlah data unik: {data[['Kedekatan', 'Hasil']].drop_duplicates().shape[0]}")

    # Menambahkan jitter untuk menyebarkan titik yang bertumpuk
    jittered_kedekatan = data['Kedekatan'] + np.random.normal(0, 0.01, size=len(data))  # Menambahkan noise kecil pada kedekatan
    jittered_hasil = data['Hasil'] + np.random.normal(0, 0.1, size=len(data))  # Menambahkan noise kecil pada hasil

    # Membuat plot
    plt.figure(figsize=(12, 8))

    # Scatter plot untuk Kedekatan vs Hasil
    scatter = plt.scatter(jittered_kedekatan, jittered_hasil, c=data['Hasil'], cmap='viridis', alpha=0.7, edgecolors='k', s=100)

    # Menambahkan label dan judul
    plt.title("Visualisasi Kedekatan vs Hasil", fontsize=16)
    plt.xlabel("Kedekatan", fontsize=12)
    plt.ylabel("Hasil", fontsize=12)

    # Menambahkan colorbar berdasarkan 'Hasil'
    plt.colorbar(scatter, label='Hasil')

    # Menambahkan grid
    plt.grid(True, linestyle='--', alpha=0.7)
    # Menyimpan gambar ke file
    plt.savefig('kmeans_visualization_iterasi1K.png')
    plt.close()
    return send_file('kmeans_visualization_iterasi1K.png', mimetype='image/png')

# Endpoint untuk visualisasi K-Means ITERASI 2----------------------------------------------------------
data_iterasi2 = pd.read_csv('iterasi2.csv')
@app.route('/Kmean/visualize2', methods=['GET'])
def visualize_kmeans_iterasi2():
    # Mengambil IPK sebagai input clustering
    ipk_values = data_iterasi2['ipk'].values.reshape(-1, 1)

    # Nilai centroid awal
    initial_centroids = [[3.02], [3.46], [3.79]]

    # K-Means Clustering dengan centroid awal
    kmeans = KMeans(n_clusters=3, init=np.array(initial_centroids), n_init=1, random_state=42)
    kmeans.fit(ipk_values)
    data_iterasi2['Cluster'] = kmeans.labels_

    # Plot data
    plt.figure(figsize=(8, 6))
    colors = ['red', 'blue', 'green']
    for cluster in range(3):
        cluster_data = data_iterasi2[data_iterasi2['Cluster'] == cluster]
        plt.scatter(
            cluster_data.index, cluster_data['ipk'], color=colors[cluster], label=f'Cluster {cluster}'
        )
    
    # Centroid plot
    plt.scatter(range(len(kmeans.cluster_centers_)), kmeans.cluster_centers_.flatten(), color='black', marker='X', s=200, label='Centroids')
    plt.title('K-Means Clustering (IPK) ITERASI 2')
    plt.xlabel('Index')
    plt.ylabel('IPK')
    plt.legend()
    plt.grid(True)

    # Simpan gambar dan kirimkan sebagai response
    plt.savefig('kmeans_visualization_iterasi2.png')
    plt.close()
    return send_file('kmeans_visualization_iterasi2.png', mimetype='image/png')

@app.route('/Kmean/visualize2K', methods=['GET'])
def visualize_kedekatan_hasil2():
    # Memuat data CSV
    data = pd.read_csv('KmeanIterasi2K.csv')  # Pastikan file CSV ada di folder yang benar

    # Mengecek jumlah data
    print(f"Jumlah data: {len(data)}")
    print(f"Jumlah data unik: {data[['Kedekatan', 'Hasil']].drop_duplicates().shape[0]}")

    # Menambahkan jitter untuk menyebarkan titik yang bertumpuk
    jittered_kedekatan = data['Kedekatan'] + np.random.normal(0, 0.01, size=len(data))  # Menambahkan noise kecil pada kedekatan
    jittered_hasil = data['Hasil'] + np.random.normal(0, 0.1, size=len(data))  # Menambahkan noise kecil pada hasil

    # Membuat plot
    plt.figure(figsize=(12, 8))

    # Scatter plot untuk Kedekatan vs Hasil
    scatter = plt.scatter(jittered_kedekatan, jittered_hasil, c=data['Hasil'], cmap='viridis', alpha=0.7, edgecolors='k', s=100)

    # Menambahkan label dan judul
    plt.title("Visualisasi Kedekatan vs Hasil", fontsize=16)
    plt.xlabel("Kedekatan", fontsize=12)
    plt.ylabel("Hasil", fontsize=12)
    
    # Menambahkan colorbar berdasarkan 'Hasil'
    plt.colorbar(scatter, label='Hasil')

    # Menambahkan grid
    plt.grid(True, linestyle='--', alpha=0.7)
    # Menyimpan gambar ke file
    plt.savefig('kmeans_visualization_iterasi2K.png')
    plt.close()
    return send_file('kmeans_visualization_iterasi2K.png', mimetype='image/png')

# Endpoint untuk visualisasi K-Means ITERASI 3-----------------------------------------------------------
@app.route('/Kmean/visualize3', methods=['GET'])
def visualize_kmeans_3():
    # Load dataset di dalam route
    try:
        data = pd.read_csv('clustered_data.csv')
    except FileNotFoundError:
        return "File 'clustered_data.csv' tidak ditemukan.", 400
    except pd.errors.EmptyDataError:
        return "File 'clustered_data.csv' kosong.", 400

    # Pastikan kolom MAPE ada dalam dataset
    if 'mape' not in data.columns:
        return "Kolom 'MAPE' tidak ditemukan dalam dataset.", 400
    
    # Ambil MAPE sebagai input clustering
    mape_values = data['mape'].values.reshape(-1, 1)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(mape_values)
    data['Cluster'] = kmeans.labels_

    # Plot hasil clustering
    plt.figure(figsize=(8, 6))
    colors = ['red', 'blue', 'green']
    for cluster in range(3):
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(cluster_data.index, cluster_data['mape'], color=colors[cluster], label=f'Cluster {cluster}')
    
    # Tambahkan centroid
    plt.scatter(range(len(kmeans.cluster_centers_)), kmeans.cluster_centers_, color='black', marker='X', s=200, label='Centroids')
    
    plt.title('K-Means Clustering (mape) ITERASI 3')
    plt.xlabel('Index')
    plt.ylabel('mape')
    plt.legend()
    plt.grid(True)

    # Simpan gambar dan kirimkan sebagai response
    filename = 'kmeans_visualization_iterasi3.png'
    plt.savefig(filename)
    plt.close()
    
    return send_file(filename, mimetype='image/png')

@app.route('/Kmean/visualize3K', methods=['GET'])
def visualize_kedekatan_hasil3():
    # Memuat data CSV
    data = pd.read_csv('KmeanIterasi2K.csv')  # Pastikan file CSV ada di folder yang benar

    # Mengecek jumlah data
    print(f"Jumlah data: {len(data)}")
    print(f"Jumlah data unik: {data[['Kedekatan', 'Hasil']].drop_duplicates().shape[0]}")

    # Menambahkan jitter untuk menyebarkan titik yang bertumpuk
    jittered_kedekatan = data['Kedekatan'] + np.random.normal(0, 0.01, size=len(data))  # Menambahkan noise kecil pada kedekatan
    jittered_hasil = data['Hasil'] + np.random.normal(0, 0.1, size=len(data))  # Menambahkan noise kecil pada hasil

    # Membuat plot
    plt.figure(figsize=(12, 8))

    # Scatter plot untuk Kedekatan vs Hasil
    scatter = plt.scatter(jittered_kedekatan, jittered_hasil, c=data['Hasil'], cmap='viridis', alpha=0.7, edgecolors='k', s=100)

    # Menambahkan label dan judul
    plt.title("Visualisasi Kedekatan vs Hasil", fontsize=16)
    plt.xlabel("Kedekatan", fontsize=12)
    plt.ylabel("Hasil", fontsize=12)
    
    # Menambahkan colorbar berdasarkan 'Hasil'
    plt.colorbar(scatter, label='Hasil')

    # Menambahkan grid
    plt.grid(True, linestyle='--', alpha=0.7)
    # Menyimpan gambar ke file
    plt.savefig('kmeans_visualization_iterasi3K.png')
    plt.close()
    return send_file('kmeans_visualization_iterasi3K.png', mimetype='image/png')
# KMEDOID-------------------------------------------------------------------------------------------
# Endpoint untuk K-Medoids (Manual)
@app.route('/Kmedoid', methods=['GET'])
def cluster_kmedoids():
    # ITERASI KE-1: Inisialisasi centroid manual
    centroids = [3.11, 3.43, 3.89]

    def assign_cluster(ipk):
        distances = [abs(ipk - centroid) for centroid in centroids]
        return np.argmin(distances)

    data['Cluster'] = data['ipk'].apply(assign_cluster)
    data['Nilai Prediksi'] = data['Cluster'].apply(lambda x: centroids[x])
    data['Nilai Selisih'] = data['ipk'] - data['Nilai Prediksi']
    data['MAPE'] = abs(data['Nilai Selisih']) / data['ipk'] * 100

    return jsonify(data.to_dict(orient='records'))

# Endpoint untuk visualisasi K-Medoids
@app.route('/Kmedoid/visualize', methods=['GET'])
def visualize_mape():
    # Read the clustered data CSV file
    data = pd.read_csv('clusetered_data_kmedoid.csv')

    # Define the centroids
    centroids = [3.11, 3.43, 3.89]

    # Function to assign clusters based on IPK
    def assign_cluster(ipk):
        distances = [abs(ipk - centroid) for centroid in centroids]
        return np.argmin(distances)

    # Assign clusters to the data based on the IPK
    data['Cluster'] = data['ipk'].apply(assign_cluster)

    # Calculate MAPE for each row (using 'IPK' vs 'Nilai Prediksi')
    data['MAPE'] = (abs(data['ipk'] - data['Nilai Prediksi']) / data['ipk']) * 100

    # Plot the data
    plt.figure(figsize=(8, 6))
    colors = ['red', 'blue', 'green']
    for cluster in range(3):
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(cluster_data.index, cluster_data['MAPE'], color=colors[cluster], label=f'Cluster {cluster}')
    
    # Plotting the centroids of clusters in MAPE space
    plt.scatter(range(len(centroids)), [np.mean(data['MAPE'][data['Cluster'] == i]) for i in range(3)],
                color='black', marker='X', s=200, label='Centroids')

    # Title and labels
    plt.title('K-Medoids Clustering (MAPE)')
    plt.xlabel('Index')
    plt.ylabel('MAPE (%)')
    plt.legend()
    plt.grid(True)


    # Simpan gambar dan kirimkan sebagai response
    plt.savefig('kmedoids_visualization.png')
    plt.close()
    return send_file('kmedoids_visualization.png', mimetype='image/png')

# KEDEKATAN 1 ---------------------------------------------------------------------------------------
@app.route('/Kmedoid/visualize1M', methods=['GET'])
def visualize_kedekatan_hasilM():
    # Memuat data CSV
    data = pd.read_csv('KmedoidIterasi1K.csv')  # Pastikan file CSV ada di folder yang benar

    # Mengecek jumlah data
    print(f"Jumlah data: {len(data)}")
    print(f"Jumlah data unik: {data[['Kedekatan', 'Hasil']].drop_duplicates().shape[0]}")

    # Menambahkan jitter untuk menyebarkan titik yang bertumpuk
    jittered_kedekatan = data['Kedekatan'] + np.random.normal(0, 0.01, size=len(data))  # Menambahkan noise kecil pada kedekatan
    jittered_hasil = data['Hasil'] + np.random.normal(0, 0.1, size=len(data))  # Menambahkan noise kecil pada hasil

    # Membuat plot
    plt.figure(figsize=(12, 8))

    # Scatter plot untuk Kedekatan vs Hasil
    scatter = plt.scatter(jittered_kedekatan, jittered_hasil, c=data['Hasil'], cmap='viridis', alpha=0.7, edgecolors='k', s=100)

    # Menambahkan label dan judul
    plt.title("Visualisasi Kedekatan vs Hasil", fontsize=16)
    plt.xlabel("Kedekatan", fontsize=12)
    plt.ylabel("Hasil", fontsize=12)
    
    # Menambahkan colorbar berdasarkan 'Hasil'
    plt.colorbar(scatter, label='Hasil')

    # Menambahkan grid
    plt.grid(True, linestyle='--', alpha=0.7)
    # Menyimpan gambar ke file
    plt.savefig('kmedoid_visualization_iterasi1K.png')
    plt.close()
    return send_file('kmedoid_visualization_iterasi1K.png', mimetype='image/png')

# KEDEKATAN 1 ---------------------------------------------------------------------------------------
@app.route('/Kmedoid/visualize2M', methods=['GET'])
def visualize_kedekatan_hasi2M():
    # Memuat data CSV
    data = pd.read_csv('KmedoidIterasi2K.csv')  # Pastikan file CSV ada di folder yang benar

    # Mengecek jumlah data
    print(f"Jumlah data: {len(data)}")
    print(f"Jumlah data unik: {data[['Kedekatan', 'Hasil']].drop_duplicates().shape[0]}")

    # Menambahkan jitter untuk menyebarkan titik yang bertumpuk
    jittered_kedekatan = data['Kedekatan'] + np.random.normal(0, 0.01, size=len(data))  # Menambahkan noise kecil pada kedekatan
    jittered_hasil = data['Hasil'] + np.random.normal(0, 0.1, size=len(data))  # Menambahkan noise kecil pada hasil

    # Membuat plot
    plt.figure(figsize=(12, 8))

    # Scatter plot untuk Kedekatan vs Hasil
    scatter = plt.scatter(jittered_kedekatan, jittered_hasil, c=data['Hasil'], cmap='viridis', alpha=0.7, edgecolors='k', s=100)

    # Menambahkan label dan judul
    plt.title("Visualisasi Kedekatan vs Hasil", fontsize=16)
    plt.xlabel("Kedekatan", fontsize=12)
    plt.ylabel("Hasil", fontsize=12)
    
    # Menambahkan colorbar berdasarkan 'Hasil'
    plt.colorbar(scatter, label='Hasil')

    # Menambahkan grid
    plt.grid(True, linestyle='--', alpha=0.7)
    # Menyimpan gambar ke file
    plt.savefig('kmedoid_visualization_iterasi2K.png')
    plt.close()
    return send_file('kmedoid_visualization_iterasi2K.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, port=5001)