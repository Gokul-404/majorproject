import streamlit as st
import pandas as pd
from src.drift_detection import detect_drift_for_your_model

st.title("📈 AI Model Drift Monitor")

if st.button("🔍 Run Drift Detection on Your Model"):
    with st.spinner("Detecting drift..."):
        is_drifted, drift_percent = detect_drift_for_your_model()
        if is_drifted:
            st.error(f"🚨 DRIFT DETECTED! {drift_percent:.1%} of features drifted.")
            st.warning("Consider retraining your model.")
        else:
            st.success("✅ No significant drift detected. Model is stable.")

st.markdown("---")
st.write("### Drift Report (Evidently AI)")
try:
    with open("../app/static/your_model_drift_report.html", "r") as f:
        html = f.read()
        st.components.v1.html(html, height=600, scrolling=True)
except:
    st.info("Run drift detection first to generate report.")