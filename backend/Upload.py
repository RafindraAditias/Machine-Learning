from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids  # Import KMedoids dari scikit-learn-extra
import numpy as np

app = Flask(__name__)
CORS(app)

# Endpoint untuk K-Means
@app.route('/Kmean', methods=['GET'])
def cluster_kmeans():
    # Membaca data dari CSV
    data = pd.read_csv('dataMahasiswa.csv')

    # Mengambil IPK sebagai input clustering
    ipk_values = data['ipk'].values.reshape(-1, 1)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(ipk_values)

    # Menambahkan hasil clustering ke dalam data
    data['Cluster'] = kmeans.labels_
    centroids = kmeans.cluster_centers_.flatten()
    data['Nilai Prediksi'] = data['Cluster'].apply(lambda x: centroids[x])
    data['Nilai Selisih'] = data['ipk'] - data['Nilai Prediksi']
    data['MAPE'] = abs(data['Nilai Selisih']) / data['ipk'] * 100

    return jsonify(data.to_dict(orient='records'))

# Endpoint untuk K-Medoids menggunakan sklearn-extra
@app.route('/Kmedoid', methods=['GET'])
def cluster_kmedoids():
    # Membaca data dari CSV
    data = pd.read_csv('dataMahasiswa.csv')

    # Mengambil IPK sebagai input clustering
    ipk_values = data['ipk'].values.reshape(-1, 1)

    # K-Medoids Clustering
    kmedoids = KMedoids(n_clusters=3, random_state=42, metric="manhattan")
    kmedoids.fit(ipk_values)

    # Menambahkan hasil clustering ke data
    data['Cluster'] = kmedoids.labels_
    centroids = kmedoids.cluster_centers_.flatten()
    data['Nilai Prediksi'] = data['Cluster'].apply(lambda x: centroids[x])
    data['Nilai Selisih'] = data['ipk'] - data['Nilai Prediksi']
    data['MAPE'] = abs(data['Nilai Selisih']) / data['ipk'] * 100

    return jsonify(data.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
