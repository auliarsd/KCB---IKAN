from models import db, SensorData, KoiType

def get_sensor_data():
    data = SensorData.query.all()
    return [{
        "temperature": d.temperature,
        "ph": d.ph,
        "created_at": d.created_at,
        "koi_type": d.koi_type.name
    } for d in data]

def add_sensor_data(data):
    new_data = SensorData(
        temperature=data['temperature'],
        ph=data['ph'],
        koi_type_id=data['koi_type_id']
    )
    db.session.add(new_data)
    db.session.commit()

def get_koi_types():
    types = KoiType.query.all()
    return [{
        "id": t.id,
        "name": t.name,
        "optimal_temp_min": t.optimal_temp_min,
        "optimal_temp_max": t.optimal_temp_max,
        "optimal_ph_min": t.optimal_ph_min,
        "optimal_ph_max": t.optimal_ph_max
    } for t in types]

def add_koi_type(data):
    new_type = KoiType(
        name=data['name'],
        optimal_temp_min=data['optimal_temp_min'],
        optimal_temp_max=data['optimal_temp_max'],
        optimal_ph_min=data['optimal_ph_min'],
        optimal_ph_max=data['optimal_ph_max']
    )
    db.session.add(new_type)
    db.session.commit()
