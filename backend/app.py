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

# Endpoint untuk visualisasi K-Means ITERASI 1
# Membaca data dari CSV
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


# Endpoint untuk visualisasi K-Means ITERASI 2
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


# Endpoint untuk visualisasi K-Means ITERASI 3
@app.route('/Kmean/visualize3', methods=['GET'])
def visualize_kmeans_3():
    # Mengambil IPK sebagai input clustering
    ipk_values = data['ipk'].values.reshape(-1, 1)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(ipk_values)
    data['Cluster'] = kmeans.labels_

    # Plot data
    plt.figure(figsize=(8, 6))
    colors = ['red', 'blue', 'green']
    for cluster in range(3):
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(cluster_data.index, cluster_data['ipk'], color=colors[cluster], label=f'Cluster {cluster}')
    plt.scatter(range(len(kmeans.cluster_centers_)), kmeans.cluster_centers_, color='black', marker='X', s=200, label='Centroids')
    plt.title('K-Means Clustering (IPK) ITERASI 3')
    plt.xlabel('Index')
    plt.ylabel('IPK')
    plt.legend()
    plt.grid(True)

    # Simpan gambar dan kirimkan sebagai response
    plt.savefig('kmeans_visualization_iterasi3.png')
    plt.close()
    return send_file('kmeans_visualization_iterasi3.png', mimetype='image/png')

# @app.route('/Kmean/visualize3', methods=['GET'])
# def visualize_kmeans_3():
#     # Load the CSV data
#     data = pd.read_csv('kh.csv')  # Make sure the file is in the right path

#     # Selecting the relevant columns (C0, C1, C2) for clustering
#     features = data[['C0', 'C1', 'C2']]

#     # K-Means Clustering
#     kmeans = KMeans(n_clusters=3, random_state=42)
#     kmeans.fit(features)
#     data['Cluster'] = kmeans.labels_

#     # Plot data
#     plt.figure(figsize=(8, 6))
#     colors = ['red', 'blue', 'green']
    
#     for cluster in range(3):
#         cluster_data = data[data['Cluster'] == cluster]
#         plt.scatter(cluster_data.index, cluster_data['C0'], color=colors[cluster], label=f'Cluster {cluster}')
    
#     plt.scatter(range(len(kmeans.cluster_centers_)), kmeans.cluster_centers_[:, 0], color='black', marker='X', s=200, label='Centroids')
#     plt.title('K-Means Clustering (C0) - Iterasi 3')
#     plt.xlabel('Index')
#     plt.ylabel('C0')
#     plt.legend()
#     plt.grid(True)

    # Save the image and send as response
    plt.savefig('kmeans_visualization_iterasi3.png')
    plt.close()
    return send_file('kmeans_visualization_iterasi3.png', mimetype='image/png')


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
@app.route('/Kmedoid/visualize2', methods=['GET'])
def visualize_kmedoids():
    centroids = [3.11, 3.43, 3.89]

    def assign_cluster(ipk):
        distances = [abs(ipk - centroid) for centroid in centroids]
        return np.argmin(distances)

    data['Cluster'] = data['ipk'].apply(assign_cluster)

    # Plot data
    plt.figure(figsize=(8, 6))
    colors = ['red', 'blue', 'green']
    for cluster in range(3):
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(cluster_data.index, cluster_data['ipk'], color=colors[cluster], label=f'Cluster {cluster}')
    plt.scatter(range(len(centroids)), centroids, color='black', marker='X', s=200, label='Centroids')
    plt.title('K-Medoids Clustering (IPK)')
    plt.xlabel('Index')
    plt.ylabel('IPK')
    plt.legend()
    plt.grid(True)

    # Simpan gambar dan kirimkan sebagai response
    plt.savefig('kmedoids_visualization.png')
    plt.close()
    return send_file('kmedoids_visualization.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5001)