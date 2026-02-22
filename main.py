import streamlit as st

st.set_page_config(page_title="Preventive Health AI", layout="centered")

# UI Styling
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: radial-gradient(circle at center, #1e232a 0%, #101114 70%);
    color: white;
}

.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 120px;
    text-align: center;
}

.stButton > button {
    background: linear-gradient(90deg, #80bfd4, #3c464e);
    color: black;
    border-radius: 40px;
    padding: 15px 40px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 Preventive Health AI")
st.write("AI-Based Multi-Domain Health Risk Detection System")

if st.button("🚀 Start Assessment"):
    st.session_state.input_data = {}
    st.switch_page("pages/1_User_Input.py")