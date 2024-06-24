from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    koi_type_id = db.Column(db.Integer, db.ForeignKey('koi_type.id'), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    ph = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

class KoiType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    optimal_temp_min = db.Column(db.Float, nullable=False)
    optimal_temp_max = db.Column(db.Float, nullable=False)
    optimal_ph_min = db.Column(db.Float, nullable=False)
    optimal_ph_max = db.Column(db.Float, nullable=False)
    sensor_data = db.relationship('SensorData', backref='koi_type', lazy=True)
