from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Path to the existing CSV file
csv_file_path = './dataMahasiswa.csv'

@app.route('/upload', methods=['POST'])
def upload_csv():
    # Get form data
    no = request.form.get('no')
    jurusan = request.form.get('jurusan')
    nama_mahasiswa = request.form.get('nama_mahasiswa')
    ipk = request.form.get('ipk')

    # Debug: Print the form data to ensure it's received correctly
    print(f"Received data - No: {no}, Jurusan: {jurusan}, Nama: {nama_mahasiswa}, IPK: {ipk}")
    
    # Check if any data is missing
    if not no or not jurusan or not nama_mahasiswa or not ipk:
        return jsonify({"error": "Missing data. All fields are required."}), 400

    # Create a new DataFrame with the form data
    new_data = {
        'no': [no],
        'jurusan': [jurusan],
        'nama_mahasiswa': [nama_mahasiswa],
        'ipk': [ipk]
    }
    df_new = pd.DataFrame(new_data)

    # Check if the CSV file exists
    if os.path.exists(csv_file_path):
        # If the file exists, append the new data
        df_existing = pd.read_csv(csv_file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(csv_file_path, index=False)
    else:
        # If the file doesn't exist, create it and save the new data
        df_new.to_csv(csv_file_path, index=False)

    return jsonify({"message": "Data uploaded successfully!", "data_preview": df_new.to_dict(orient='records')}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
