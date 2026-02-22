import streamlit as st

st.set_page_config(page_title="Step 1 - Basic Info", layout="centered")

# =================== PREMIUM HEALTH APP CSS ===================
st.markdown("""
<style>

/* Hide default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* App Background */
.stApp {
    background: linear-gradient(145deg, #0f172a, #111827);
    font-family: 'Segoe UI', sans-serif;
}

/* Main container */
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

/* Section Headings */
.section-title {
    color: #22d3ee;
    font-size: 18px;
    font-weight: 600;
    margin-top: 25px;
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

/* Focus effect */
.stNumberInput input:focus {
    border: 1px solid #06b6d4 !important;
    box-shadow: 0 0 10px rgba(6,182,212,0.4) !important;
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
    margin-top: 20px;
}

/* Button hover */
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(59,130,246,0.4);
}

/* Glow Divider */
.divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #3b82f6, transparent);
    margin: 20px 0;
}

</style>
""", unsafe_allow_html=True)

# =================== UI ===================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.title("Step 1: Basic Health Information")

if "input_data" not in st.session_state:
    st.session_state.input_data = {}

# -------- Personal Section --------
st.markdown('<div class="section-title">👤 Personal Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 1, 120)
with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])

col3, col4 = st.columns(2)
with col3:
    height_cm = st.number_input("Height (cm)", 100.0, 250.0)
with col4:
    weight_kg = st.number_input("Weight (kg)", 30.0, 200.0)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# -------- Vitals Section --------
st.markdown('<div class="section-title">🫀 Vital Signs</div>', unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    systolic_bp = st.number_input("Systolic BP", 50, 250)
with col6:
    diastolic_bp = st.number_input("Diastolic BP", 30, 150)

col7, col8 = st.columns(2)
with col7:
    heart_rate = st.number_input("Heart Rate", 30, 200)
with col8:
    spo2 = st.number_input("SpO2", 50, 100)

col9, col10 = st.columns(2)
with col9:
    blood_sugar = st.number_input("Blood Sugar", 50, 500)
with col10:
    cholesterol = st.number_input("Cholesterol", 50, 500)

body_temperature = st.number_input("Body Temperature (°C)", 30.0, 45.0)

# -------- Continue Button --------
if st.button("Next Page➜"):
    st.session_state.input_data.update({
        "age": age,
        "gender": gender,
        "height_cm": height_cm,
        "weight_kg": weight_kg,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "heart_rate": heart_rate,
        "blood_sugar": blood_sugar,
        "cholesterol": cholesterol,
        "spo2": spo2,
        "body_temperature": body_temperature,
    })
    st.switch_page("pages/2_Lifestyle_Symptoms.py")

st.markdown('</div>', unsafe_allow_html=True)