from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans

app = Flask(__name__)
CORS(app)  # Tambahkan ini untuk mengizinkan semua permintaan CORS

@app.route('/cluster', methods=['GET'])
def cluster():
    data = pd.read_csv('dataMahasiswa2.csv')
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