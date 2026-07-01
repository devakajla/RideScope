import joblib
import numpy as np

_duration_bundle = None
_rider_bundle = None

def load_models():
    global _duration_bundle, _rider_bundle
    _duration_bundle = joblib.load("trained_models/duration_model.pkl")
    _rider_bundle = joblib.load("trained_models/rider_type_model.pkl")

def predict_duration(ride_type, hour, day_of_week, month, distance_km):
    model = _duration_bundle['model']
    le = _duration_bundle['label_encoders']
    features = np.array([[
        le['ride_type'].transform([ride_type])[0],
        hour,
        le['day_of_week'].transform([day_of_week])[0],
        month,
        distance_km
    ]])
    prediction = model.predict(features)[0]
    return round(prediction, 2)

def predict_rider_type(ride_type, trip_duration, hour, day_of_week, month, distance_km):
    model = _rider_bundle['model']
    le = _rider_bundle['label_encoders']
    features = np.array([[
        le['ride_type'].transform([ride_type])[0],
        trip_duration,
        hour,
        le['day_of_week'].transform([day_of_week])[0],
        month,
        distance_km
    ]])
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    predicted_label = le['target'].inverse_transform([prediction])[0]
    return {
        "predicted_type": predicted_label,
        "probability": {
            "casual": round(float(proba[0]), 2),
            "member": round(float(proba[1]), 2)
        }
    }

