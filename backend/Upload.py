from flask import Flask, request, jsonify
import csv

app = Flask(__name__)
CSV_FILE = 'dataMahasiswa.csv'

# READ: Mendapatkan data dari CSV
@app.route('/data', methods=['GET'])
def get_data():
    data = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return jsonify(data)

# CREATE: Menambahkan data baru ke CSV
@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.json
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['no', 'jurusan', 'nama_mahasiswa', 'ipk']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_data)
    return jsonify({"message": "Data added successfully"}), 201

# UPDATE: Memperbarui data berdasarkan 'no'
@app.route('/data/<no>', methods=['PUT'])
def update_data(no):
    updated_data = request.json
    data = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['no'] == no:
                row.update(updated_data)
            data.append(row)
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return jsonify({"message": "Data updated successfully"})

# DELETE: Menghapus data berdasarkan 'no'
@app.route('/data/<no>', methods=['DELETE'])
def delete_data(no):
    data = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['no'] != no:
                data.append(row)
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return jsonify({"message": "Data deleted successfully"})

if __name__ == '__main__':
    # Membuat file CSV dengan header jika belum ada
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            pass
    except FileNotFoundError:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['no', 'jurusan', 'nama_mahasiswa', 'ipk']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    app.run(debug=True)
