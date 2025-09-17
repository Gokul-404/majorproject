import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import os

st.title("🛡️ Cyber Threat Detection (NSL-KDD)")

@st.cache_resource
def load_threat_model():
    if os.path.exists('../models/threat_model.pkl'):
        model = joblib.load('../models/threat_model.pkl')
        le_attack = joblib.load('../models/le_attack.pkl')
        return model, le_attack
    else:
        st.error("⚠️ Threat model not found. Run src/threat_detection.py first.")
        return None, None

model, le_attack = load_threat_model()

if model:
    st.success("✅ Threat detection model loaded.")
    
    # Simulate real-time prediction
    if st.button("⚡ Simulate Real-Time Threat Prediction"):
        import numpy as np
        sample = np.random.rand(1, 41)  # 41 NSL-KDD features
        pred = model.predict(sample)[0]
        attack_name = le_attack.inverse_transform([pred])[0]
        st.subheader(f"🚨 Detected Threat: `{attack_name}`")
        
        # Map to cloud service
        cloud_map = {
            'normal': '✅ Normal Traffic',
            'dos': '☁️ EC2 / VMSS Overload',
            'probe': '☁️ S3 / Blob Enumeration',
            'r2l': '☁️ IAM / Azure AD Escalation',
            'u2r': '☁️ RDS / CosmosDB Injection'
        }
        st.info(f"**Simulated Cloud Target**: {cloud_map.get(attack_name.lower(), 'Unknown')}")

    # Show attack distribution
    if st.checkbox("📊 Show Attack Type Distribution"):
        attack_counts = pd.Series(le_attack.classes_).value_counts()
        fig = px.pie(names=attack_counts.index, values=attack_counts.values, title="NSL-KDD Attack Type Distribution")
        st.plotly_chart(fig)