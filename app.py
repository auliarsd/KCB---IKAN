from flask import Flask, jsonify, request
from models import db, SensorData, KoiType
from controllers import get_sensor_data, add_sensor_data, get_koi_types, add_koi_type

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

@app.route('/data', methods=['GET'])
def data():
    return jsonify(get_sensor_data())

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json
    add_sensor_data(data)
    return jsonify({"message": "Data added successfully"}), 201

@app.route('/koi_types', methods=['GET'])
def koi_types():
    return jsonify(get_koi_types())

@app.route('/koi_types', methods=['POST'])
def add_koi():
    data = request.json
    add_koi_type(data)
    return jsonify({"message": "Koi type added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
