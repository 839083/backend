import os
import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Step 3 - Prediction", layout="centered")

# ===================== REFINED THEME CSS =====================
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: linear-gradient(145deg, #0f172a, #111827);
    font-family: 'Segoe UI', sans-serif;
}

/* Main container */
.block-container {
    max-width: 950px;
    padding-top: 40px;
}

/* Glass container */
.glass-card {
    background: rgba(255,255,255,0.05);
    border-radius: 25px;
    padding: 35px;
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 25px 60px rgba(0,0,0,0.6);
}

/* Title */
h1 {
    color: #f8fafc !important;
    font-weight: 600;
    text-align: center;
    margin-bottom: 25px;
}

/* Risk Card */
.risk-card {
    background: rgba(255,255,255,0.06);
    padding: 22px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.06);
    transition: all 0.3s ease;
}

.risk-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(59,130,246,0.2);
}

/* Risk title */
.risk-title {
    color: #94a3b8;
    font-size: 14px;
    letter-spacing: 0.5px;
}

/* Risk value */
.risk-value {
    font-size: 22px;
    font-weight: 600;
    margin-top: 5px;
}

/* Recommendation box */
.recommend-box {
    background: rgba(59,130,246,0.08);
    border: 1px solid rgba(59,130,246,0.3);
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
}

/* Progress bar thickness */
.stProgress > div > div > div > div {
    height: 8px;
}

</style>
""", unsafe_allow_html=True)

# ===================== TensorFlow Optimization =====================
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"

tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)

@st.cache_resource
def load_objects():
    model = tf.keras.models.load_model("final_advanced_multi_domain_model.keras")
    scaler = joblib.load("scaler.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
    label_encoders = joblib.load("multi_label_encoders.pkl")
    return model, scaler, feature_columns, label_encoders

model, scaler, feature_columns, label_encoders = load_objects()

# ===================== PAGE START =====================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.title("AI Health Risk Analysis")

if "input_data" not in st.session_state:
    st.switch_page("app.py")

# ===================== MODEL PREDICTION =====================
df = pd.DataFrame([st.session_state.input_data])
df["bmi"] = df["weight_kg"] / ((df["height_cm"] / 100) ** 2)

df = pd.get_dummies(df)
df = df.reindex(columns=feature_columns, fill_value=0)

df_scaled = scaler.transform(df)
predictions = model.predict(df_scaled)

risk_names = ["heart_risk", "metabolic_risk", "stress_risk", "lung_risk", "lifestyle_risk"]

result = {}

for i, risk in enumerate(risk_names):
    pred_class = np.argmax(predictions[i], axis=1)
    label = label_encoders[risk].inverse_transform(pred_class)[0]
    confidence = float(np.max(predictions[i]))

    result[risk] = label
    result[f"{risk}_confidence"] = round(confidence, 3)

# ===================== RISK DISPLAY =====================
st.subheader("📊 Risk Overview")

cols = st.columns(3)

def get_color(risk):
    if risk == "High":
        return "#ef4444"   # soft red
    elif risk == "Medium":
        return "#f59e0b"   # amber
    else:
        return "#22c55e"   # soft green

for idx, risk in enumerate(risk_names):
    with cols[idx % 3]:
        color = get_color(result[risk])

        st.markdown(f"""
        <div class="risk-card">
            <div class="risk-title">{risk.replace('_',' ').title()}</div>
            <div class="risk-value" style="color:{color};">
                {result[risk]}
            </div>
            <div style="color:#94a3b8; font-size:13px; margin-top:6px;">
                Confidence: {result[risk + "_confidence"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(result[risk + "_confidence"])

# ===================== RECOMMENDATIONS =====================
st.subheader("📋 Personalized Recommendations")

recs = []

if result["heart_risk"] == "High":
    recs += ["❤️ Consult cardiologist", "🥗 Reduce salt intake"]

if result["metabolic_risk"] == "High":
    recs += ["🍬 Reduce sugar intake", "🏃 Exercise regularly"]

if result["stress_risk"] == "High":
    recs += ["😴 Improve sleep schedule", "🧘 Practice meditation"]

if result["lung_risk"] == "High":
    recs += ["🚭 Avoid smoking", "🫁 Monitor oxygen levels"]

if result["lifestyle_risk"] == "High":
    recs += ["🥦 Balanced diet", "🏋 Structured workout routine"]

if not recs:
    recs.append("✅ Maintain your healthy lifestyle.")

st.markdown('<div class="recommend-box">', unsafe_allow_html=True)

for r in recs:
    st.write(r)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)