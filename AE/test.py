from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Path to your JSON file
JSON_FILE_PATH = 'data.json'

# Helper function to read from the JSON file
def read_json_file():
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    else:
        return {}

# Helper function to write to the JSON file
def write_json_file(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

# Route to save data to the JSON file
@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()  # Get JSON data from the POST request
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Load existing data from the file
    existing_data = read_json_file()

    # Optionally, you can append or update the existing data
    # Here we append the new data
    existing_data.update(data)

    # Write the updated data back to the file
    write_json_file(existing_data)

    return jsonify({"message": "Data saved successfully"}), 200

# Route to get data from the JSON file
@app.route('/data', methods=['GET'])
def get_data():
    data = read_json_file()
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
