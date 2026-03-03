# import streamlit as st
# import streamlit.components.v1 as components

# # --- 1. PAGE CONFIG & STYLING ---
# st.set_page_config(page_title="Structural Predictor", layout="centered")

# # Injecting Custom CSS to match your Tailwind design
# st.markdown("""
#     <style>
#     /* Global Styles */
#     .stApp { background-color: #f6f7f8; }
#     [data-testid="stHeader"] { display: none; } /* Hide default streamlit header */
    
#     /* Custom Header */
#     .app-header {
#         background-color: white;
#         padding: 15px;
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         border-bottom: 1px solid #e2e8f0;
#         position: sticky; top: 0; z-index: 100;
#     }
    
#     /* Section Headers */
#     .section-title {
#         color: #1e293b; font-weight: 700; font-size: 1.2rem;
#         margin-top: 20px; display: flex; align-items: center; gap: 8px;
#     }
#     .group-label {
#         color: #64748b; font-size: 0.7rem; font-weight: 800;
#         text-transform: uppercase; letter-spacing: 1px; margin-top: 15px;
#     }

#     /* Result Cards */
#     .res-card {
#         background: white; padding: 15px; border-radius: 12px;
#         border: 1px solid #f1f5f9; text-align: left;
#         box-shadow: 0 1px 2px rgba(0,0,0,0.05);
#     }
#     .res-label { color: #64748b; font-size: 0.75rem; margin-bottom: 4px; }
#     .res-val { font-size: 1.25rem; font-weight: 800; }

#     /* Action Box */
#     .action-box {
#         background-color: #fff7ed; border: 1px solid #fed7aa;
#         padding: 15px; border-radius: 12px; margin-top: 20px;
#         display: flex; align-items: center; gap: 12px;
#     }

#     /* Custom Button Style */
#     div.stButton > button {
#         width: 100%; background-color: #2b8cee !important; color: white !important;
#         border-radius: 10px !important; height: 3em !important; font-weight: bold !important;
#         border: none !important; box-shadow: 0 4px 6px -1px rgba(43, 140, 238, 0.3);
#     }
#     .secondary-btn button {
#         background-color: #1e293b !important;
#     }
#     </style>
    
#     <div class="app-header">
#         <span style="color:#2b8cee; font-size:24px;">☰</span>
#         <b style="font-size: 18px;">Structural Performance Predictor</b>
#         <span style="color:#64748b; font-size:20px;">ⓘ</span>
#     </div>
# """, unsafe_allow_html=True)

# # --- 2. INPUT PARAMETERS ---
# st.markdown('<div class="section-title">📝 Input Parameters</div>', unsafe_allow_html=True)

# # Material Properties
# st.markdown('<div class="group-label">Material Properties</div>', unsafe_allow_html=True)
# c1, c2 = st.columns(2)
# fc = c1.number_input("Concrete fc (MPa)", value=25)
# fy = c2.number_input("Steel fy (MPa)", value=415)

# # Environmental Factors
# st.markdown('<div class="group-label">Environmental Factors</div>', unsafe_allow_html=True)
# c3, c4 = st.columns(2)
# z = c3.number_input("Seismic Coeff z", value=0.20, format="%.2f")
# r = c4.number_input("Reduction R", value=8)
# c5, c6 = st.columns(2)
# v = c5.number_input("Wind Speed v (m/s)", value=45)
# w = c6.number_input("Live Load W (kN/m²)", value=2.5)

# # Geometry
# st.markdown('<div class="group-label">Geometry & Dimensions</div>', unsafe_allow_html=True)
# c7, c8 = st.columns(2)
# la = c7.number_input("Long Axis La (m)", value=24)
# lb = c8.number_input("Short Axis Lb (m)", value=18)
# c9, c10 = st.columns(2)
# n = c9.number_input("No. of Story n", value=10)
# h = c10.number_input("Total Height H (m)", value=32)

# c11, c12 = st.columns(2)
# Hgf = c11.number_input("GF Height Hgf (m)", value=4.5)
# a = c12.number_input("Floor Area A (m²)", value=432)

# # Geometry
# st.markdown('<div class="group-label">Structural Details</div>', unsafe_allow_html=True)
# c13, c14 = st.columns(2)
# p = c13.number_input("Rebar Ratio p (%)", value=1.2)
# ag = c14.number_input("Gross Area Ag (m²)", value=0.25)

# # Predict Button
# if st.button("📊 PREDICT PERFORMANCE"):
#     # --- 3. PREDICTION RESULTS (Simulated) ---
#     st.markdown('<div class="group-label">Prediction Results</div>', unsafe_allow_html=True)
#     r1, r2 = st.columns(2)
#     with r1:
#         st.markdown('<div class="res-card"><div class="res-label">Column Fail %</div><div class="res-val" style="color:#ef4444">10.0%</div></div>', unsafe_allow_html=True)
#     with r2:
#         st.markdown('<div class="res-card"><div class="res-label">Max Story Drift</div><div class="res-val" style="color:#f97316">0.0092</div></div>', unsafe_allow_html=True)
    
#     r3, r4 = st.columns(2)
#     with r3:
#         st.markdown('<div class="res-card"><div class="res-label">Max Story Sway</div><div class="res-val" style="color:#22c55e">0.0072</div></div>', unsafe_allow_html=True)
#     with r4:
#         st.markdown('<div class="res-card"><div class="res-label">Torsional Irreg.</div><div class="res-val" style="color:#2b8cee">1.12</div></div>', unsafe_allow_html=True)

#     st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
#     st.button("⌨️ CALCULATE LIMITS")
#     st.markdown('</div>', unsafe_allow_html=True)

#     # --- 4. RISK ASSESSMENT (Circular Charts) ---
#     st.markdown('<div class="section-title">📊 Risk Assessment</div>', unsafe_allow_html=True)
    
#     # We use a component to render the custom circular CSS
#     risk_html = """
#     <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-family: sans-serif; text-align: center; background:transparent;">
#         <div>
#             <div style="width:80px; height:80px; border-radius:50%; background: conic-gradient(#ef4444 36deg, #e2e8f0 0); margin:auto; display:flex; align-items:center; justify-content:center;">
#                 <div style="width:65px; height:65px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">10%</div>
#             </div>
#             <div style="font-size:10px; font-weight:bold; margin-top:8px;">COLUMN FAILURE</div>
#             <div style="font-size:8px; color:#ef4444; font-weight:bold; background:#fee2e2; padding:2px 5px; border-radius:10px; display:inline-block;">HIGH RISK</div>
#         </div>
#         <div>
#             <div style="width:80px; height:80px; border-radius:50%; background: conic-gradient(#f97316 330deg, #e2e8f0 0); margin:auto; display:flex; align-items:center; justify-content:center;">
#                 <div style="width:65px; height:65px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">0.92</div>
#             </div>
#             <div style="font-size:10px; font-weight:bold; margin-top:8px;">DRIFT RATIO</div>
#             <div style="font-size:8px; color:#f97316; font-weight:bold; background:#ffedd5; padding:2px 5px; border-radius:10px; display:inline-block;">MODERATE</div>
#         </div>
#         <div>
#             <div style="width:80px; height:80px; border-radius:50%; background: conic-gradient(blue 300deg, #e2e8f0 0); margin:auto; display:flex; align-items:center; justify-content:center;">
#                 <div style="width:65px; height:65px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">0.72</div>
#             </div>
#             <div style="font-size:10px; font-weight:bold; margin-top:8px;">Sway Ratio</div>
#             <div style="font-size:8px; color:blue; font-weight:bold; background:#fee2e2; padding:2px 5px; border-radius:10px; display:inline-block;">LOW RISK</div>
#         </div>
#         <div>
#             <div style="width:80px; height:80px; border-radius:50%; background: conic-gradient(green 170deg, #e2e8f0 0); margin:auto; display:flex; align-items:center; justify-content:center;">
#                 <div style="width:65px; height:65px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">0.48</div>
#             </div>
#             <div style="font-size:10px; font-weight:bold; margin-top:8px;">Torsion Ratio</div>
#             <div style="font-size:8px; color:green; font-weight:bold; background:#ffedd5; padding:2px 5px; border-radius:10px; display:inline-block;">VERY LOW</div>
#         </div>
#     </div>
#     """
#     components.html(risk_html, height=300)

#     # Action Required Box
#     st.markdown("""
#         <div class="action-box">
#             <span style="font-size:24px;">⚠️</span>
#             <div>
#                 <b style="color: #9a3412; font-size:14px;">Action Required</b><br>
#                 <span style="color: #c2410c; font-size:13px;">Require a Detailed Structural Investigation</span>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

# # --- 5. ABOUT SECTION ---
# st.markdown('<br><hr>', unsafe_allow_html=True)
# st.markdown("**About this Application**")
# st.info("🎓 Developed for M.Sc. research at BUET.")
# st.info("📊 Model trained on 400+ RC structure designs.")
# st.write("📧 Contact: [khaled.ce18@gmail.com](mailto:khaled.ce18@gmail.com)")


######################################################3

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib
import numpy as np

# --- 0. SETTINGS & MODEL LOADING ---
st.set_page_config(page_title="Structural Predictor", layout="centered")

# Set Risk Thresholds as variables (as requested)
T_VERY_LOW = 0.25
T_LOW = 0.50
T_MODERATE = 0.75
MODEL_PATH = "column_overstress_gpr_model.joblib"

@st.cache_resource
def load_model():
    # Ensure model.joblib is in the same folder
    return joblib.load(MODEL_PATH)

model = load_model()

# --- 1. STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #f6f7f8; }
    [data-testid="stHeader"] { display: none; }
    .app-header {
        background-color: white; padding: 15px; display: flex;
        justify-content: space-between; align-items: center;
        border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 100;
    }
    .section-title { color: #1e293b; font-weight: 700; font-size: 1.2rem; margin-top: 20px; }
    .group-label { color: #64748b; font-size: 0.7rem; font-weight: 800; text-transform: uppercase; margin-top: 15px; }
    
    /* Result Cards */
    .res-card { background: white; padding: 15px; border-radius: 12px; border: 1px solid #f1f5f9; }
    .res-label { color: #64748b; font-size: 0.75rem; }
    .res-val { font-size: 1.25rem; font-weight: 800; }

    /* Button Styling */
    div.stButton > button {
        width: 100%; background-color: #2b8cee !important; color: white !important;
        border-radius: 10px !important; height: 3em !important; font-weight: bold !important;
        border: none !important;
    }
    </style>
    <div class="app-header">
        <span style="color:#2b8cee; font-size:24px;">☰</span>
        <b style="font-size: 18px;">Structural Performance Predictor</b>
        <span style="color:#64748b; font-size:20px;">ⓘ</span>
    </div>
""", unsafe_allow_html=True)

# --- 2. INPUT PARAMETERS ---
st.markdown('<div class="section-title">📝 Input Parameters</div>', unsafe_allow_html=True)

# Material Properties
st.markdown('<div class="group-label">Material Properties</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
fc = c1.number_input("Concrete fc (MPa)", value=25.0)
# fy = c2.number_input("Steel fy (MPa)", value=415.0) # Not in model X

# Environmental Factors
st.markdown('<div class="group-label">Environmental Factors</div>', unsafe_allow_html=True)
c3, c4 = st.columns(2)
z = c3.number_input("Seismic Coeff z", value=0.20, format="%.2f")
r = c4.number_input("Reduction R", value=8.0)
# v = st.number_input("Wind Speed v (m/s)", value=45.0) # Not in model X
# w = st.number_input("Live Load W (kN/m²)", value=2.5) # Not in model X

# Geometry & Dimensions
st.markdown('<div class="group-label">Geometry & Dimensions</div>', unsafe_allow_html=True)
c7, c8 = st.columns(2)
# la = c7.number_input("Long Axis La (m)", value=24.0) # Not in model X
lb = c8.number_input("Short Axis Lb (m)", value=18.0)

c9, c10 = st.columns(2)
n = c9.number_input("No. of Story n", value=10.0)
# h = c10.number_input("Total Height H (m)", value=32.0) # Not in model X

c11, c12 = st.columns(2)
Hgf = c11.number_input("GF Height Hgf (m)", value=4.5)
a = c12.number_input("Floor Area A (m²)", value=432.0)

# Structural Details
st.markdown('<div class="group-label">Structural Details</div>', unsafe_allow_html=True)
c13, c14 = st.columns(2)
p = c13.number_input("Rebar Ratio p (%)", value=1.2)
# ag = c14.number_input("Gross Area Ag (m²)", value=0.25) # Not in model X

# --- 3. PREDICTION LOGIC ---
if st.button("📊 PREDICT PERFORMANCE"):
    
    # Prepare data for model (must match exactly the 8 columns used in X)
    input_df = pd.DataFrame([[fc, lb, n, z, r, Hgf, a, p]], 
        columns=[
            'Compressieve Strength of Concrete, fc (Mpa)',
            'Dimension of Short Axis, Lb (m)',
            'No of Story, n',
            'Seismic Zone Coefficient, z',
            'Response Reduction Factor, R',
            'GF Story Height, Hgf (m)',
            'Typical Floor Area, A (sqm)',
            'Average Column Rebar Percentage, p (%)'
        ])

    # Model prediction (returns fraction)
    prediction_raw = model.predict(input_df)[0]
    # Ensure it stays within 0-1 range for the visual logic
    prediction = max(0, min(1, prediction_raw)) 
    
    # Determine Risk Category and Colors
    if prediction < T_VERY_LOW:
        label, color, bg = "VERY LOW", "#2b8cee", "#eff6ff"
    elif prediction < T_LOW:
        label, color, bg = "LOW RISK", "#22c55e", "#f0fdf4"
    elif prediction < T_MODERATE:
        label, color, bg = "MODERATE", "#f97316", "#fff7ed"
    else:
        label, color, bg = "HIGH RISK", "#ef4444", "#fef2f2"

    # Display Results
    st.markdown('<div class="group-label">Prediction Results</div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="res-card">
            <div class="res-label">Column Overstressed Percentage</div>
            <div class="res-val" style="color:{color}">{prediction*100:.2f}%</div>
        </div>
    """, unsafe_allow_html=True)

    # Risk Assessment Visualization
    st.markdown('<div class="section-title">📊 Risk Assessment</div>', unsafe_allow_html=True)
    
    # Dynamic Gauge (conic-gradient calculation)
    deg = prediction * 360
    risk_html = f"""
    <div style="text-align: center; font-family: sans-serif;">
        <div style="width:120px; height:120px; border-radius:50%; background: conic-gradient({color} {deg}deg, #e2e8f0 0); margin:auto; display:flex; align-items:center; justify-content:center;">
            <div style="width:90px; height:90px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:18px;">{prediction*100:.1f}%</div>
        </div>
        <div style="font-size:12px; font-weight:bold; margin-top:10px;">COLUMN FAILURE</div>
        <div style="font-size:10px; color:{color}; font-weight:bold; background:{bg}; padding:4px 10px; border-radius:12px; display:inline-block; margin-top:5px;">{label}</div>
    </div>
    """
    components.html(risk_html, height=200)

    # Conditional Warning
    if prediction >= T_MODERATE:
        st.error("**Action Required:** Detailed Structural Investigation Recommended.")