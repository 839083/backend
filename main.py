from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import pandas as pd
import numpy as np
import joblib

app = FastAPI()

# Load model and preprocessing
model = tf.keras.models.load_model("final_advanced_multi_domain_model.keras")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")
label_encoders = joblib.load("multi_label_encoders.pkl")

# ----------------------------
# Request Schema
# ----------------------------
class HealthInput(BaseModel):
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    systolic_bp: int
    diastolic_bp: int
    heart_rate: int
    blood_sugar: int
    cholesterol: int
    spo2: int
    body_temperature: float
    smoking: str
    alcohol: str
    exercise_level: str
    diet_type: str
    sleep_hours: float
    stress_level: str
    screen_time_hours: float
    water_intake_l: float
    
    fatigue: int
    mild_headache: int
    occasional_chest_discomfort: int
    frequent_urination: int
    mild_breathlessness: int
    dry_cough: int
    weight_gain: int
    weight_loss: int
    blurred_vision: int
    dizziness: int
    sleep_disturbance: int
    irregular_heartbeat: int
    leg_swelling: int
    loss_of_appetite: int

# ----------------------------
# Recommendation Engine
# ----------------------------
def generate_recommendations(risks, data):
    recs = []

    if risks["heart_risk"] == "High":
        recs.append("Consult cardiologist")
        recs.append("Reduce salt intake")
    
    if risks["metabolic_risk"] == "High":
        recs.append("Reduce sugar consumption")
        recs.append("Increase physical activity")

    if risks["stress_risk"] == "High":
        recs.append("Improve sleep schedule")
        recs.append("Practice stress management")

    if risks["lung_risk"] == "High":
        recs.append("Avoid smoking")
        recs.append("Get lung checkup if symptoms persist")

    if risks["lifestyle_risk"] == "High":
        recs.append("Start structured exercise plan")
        recs.append("Improve diet quality")

    if not recs:
        recs.append("Maintain current healthy lifestyle")

    return recs

# ----------------------------
# Prediction Endpoint
# ----------------------------
@app.post("/predict")
def predict(data: HealthInput):

    input_dict = data.dict()

    # Create DataFrame
    df = pd.DataFrame([input_dict])

    # Compute BMI
    df["bmi"] = df["weight_kg"] / ((df["height_cm"]/100) ** 2)

    # One-hot encoding
    df = pd.get_dummies(df)

    # Align columns
    df = df.reindex(columns=feature_columns, fill_value=0)

    # Scale
    df_scaled = scaler.transform(df)

    # Predict
    predictions = model.predict(df_scaled)

    output = {}
    risk_names = ["heart_risk","metabolic_risk","stress_risk","lung_risk","lifestyle_risk"]

    for i, risk in enumerate(risk_names):
        pred_class = np.argmax(predictions[i], axis=1)
        label = label_encoders[risk].inverse_transform(pred_class)[0]
        confidence = float(np.max(predictions[i]))
        output[risk] = label
        output[risk + "_confidence"] = round(confidence, 3)

    # Generate recommendations
    recs = generate_recommendations(output, input_dict)

    return {
        "risks": output,
        "recommendations": recs
    }

@app.get("/")
def root():
    return {"message": "Preventive Health API Running"}