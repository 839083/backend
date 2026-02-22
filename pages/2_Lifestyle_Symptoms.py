import streamlit as st

st.set_page_config(page_title="Step 2 - Lifestyle", layout="centered")

# ===================== PREMIUM HEALTH APP CSS =====================
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: linear-gradient(145deg, #0f172a, #111827);
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    max-width: 850px;
    padding-top: 40px;
}

/* Glass Card */
.glass-card {
    background: rgba(255,255,255,0.04);
    border-radius: 25px;
    padding: 40px;
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}

/* Title */
h1 {
    color: #f1f5f9 !important;
    font-weight: 600;
    text-align: center;
    margin-bottom: 30px;
}

/* Section title */
.section-title {
    color: #22d3ee;
    font-size: 18px;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 15px;
}

/* Labels */
label {
    color: #94a3b8 !important;
    font-weight: 500 !important;
}

/* Inputs */
.stNumberInput input, 
.stSelectbox div {
    background-color: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(59,130,246,0.3) !important;
    border-radius: 14px !important;
    color: #f1f5f9 !important;
}

/* Focus glow */
.stNumberInput input:focus {
    border: 1px solid #06b6d4 !important;
    box-shadow: 0 0 10px rgba(6,182,212,0.4) !important;
}

/* Divider */
.divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #3b82f6, transparent);
    margin: 20px 0;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white;
    border-radius: 40px;
    padding: 14px;
    font-size: 16px;
    font-weight: 600;
    border: none;
    transition: all 0.3s ease;
    margin-top: 25px;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(59,130,246,0.4);
}

</style>
""", unsafe_allow_html=True)

# ===================== UI START =====================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.title("Step 2: Lifestyle & Symptoms")

if "input_data" not in st.session_state:
    st.switch_page("app.py")

# ---------------- Lifestyle Section ----------------
st.markdown('<div class="section-title">🏃 Lifestyle Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    smoking = st.selectbox("Smoking", ["Yes", "No"])
    exercise_level = st.selectbox("Exercise Level", ["Low", "Medium", "High"])
    sleep_hours = st.number_input("Sleep Hours", 0, 24)
    screen_time_hours = st.number_input("Screen Time (hours)", 0, 24)

with col2:
    alcohol = st.selectbox("Alcohol", ["Yes", "No"])
    diet_type = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian"])
    stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])
    water_intake_l = st.number_input("Water Intake (litres)", 0.0, 10.0)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------- Symptoms Section ----------------
st.markdown('<div class="section-title">🩺 Symptoms</div>', unsafe_allow_html=True)

def yes_no(label):
    return 1 if st.selectbox(label, ["No", "Yes"]) == "Yes" else 0

col3, col4 = st.columns(2)

with col3:
    fatigue = yes_no("Fatigue")
    mild_headache = yes_no("Mild Headache")
    occasional_chest_discomfort = yes_no("Occasional Chest Discomfort")
    frequent_urination = yes_no("Frequent Urination")
    mild_breathlessness = yes_no("Mild Breathlessness")
    dry_cough = yes_no("Dry Cough")
    weight_gain = yes_no("Weight Gain")

with col4:
    weight_loss = yes_no("Weight Loss")
    blurred_vision = yes_no("Blurred Vision")
    dizziness = yes_no("Dizziness")
    sleep_disturbance = yes_no("Sleep Disturbance")
    irregular_heartbeat = yes_no("Irregular Heartbeat")
    leg_swelling = yes_no("Leg Swelling")
    loss_of_appetite = yes_no("Loss of Appetite")

# ---------------- Continue Button ----------------
if st.button("Click for Prediction ➜"):
    st.session_state.input_data.update({
        "smoking": smoking,
        "alcohol": alcohol,
        "exercise_level": exercise_level,
        "diet_type": diet_type,
        "sleep_hours": sleep_hours,
        "stress_level": stress_level,
        "screen_time_hours": screen_time_hours,
        "water_intake_l": water_intake_l,
        "fatigue": fatigue,
        "mild_headache": mild_headache,
        "occasional_chest_discomfort": occasional_chest_discomfort,
        "frequent_urination": frequent_urination,
        "mild_breathlessness": mild_breathlessness,
        "dry_cough": dry_cough,
        "weight_gain": weight_gain,
        "weight_loss": weight_loss,
        "blurred_vision": blurred_vision,
        "dizziness": dizziness,
        "sleep_disturbance": sleep_disturbance,
        "irregular_heartbeat": irregular_heartbeat,
        "leg_swelling": leg_swelling,
        "loss_of_appetite": loss_of_appetite,
    })
    st.switch_page("pages/3_Prediction.py")

st.markdown('</div>', unsafe_allow_html=True)