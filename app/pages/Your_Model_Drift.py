import streamlit as st
import joblib
import pandas as pd
from src.drift_detection import detect_drift_for_your_model

st.title("📊 Your AI Model Performance & Drift")

@st.cache_resource
def load_your_model():
    return joblib.load('../models/your_ai_model.pkl')

try:
    model = load_your_model()
    st.success("✅ Your Phishing URL Classifier loaded.")

    if st.button("🧪 Test Model Prediction"):
        sample = [[120, 1, 0, 2]]  # url_length, has_ip, has_at, redirect_count
        pred = model.predict(sample)[0]
        prob = model.predict_proba(sample)[0]
        result = "Phishing" if pred == 1 else "Safe"
        st.write(f"**Prediction**: {result}")
        st.write(f"**Confidence**: Safe {prob[0]:.2%} | Phishing {prob[1]:.2%}")

    st.markdown("---")
    st.subheader("📉 Drift Analysis")
    if st.button("🔍 Analyze Drift for Your Model"):
        is_drifted, drift_percent = detect_drift_for_your_model()
        if is_drifted:
            st.error(f"🚨 DRIFT ALERT: {drift_percent:.1%} of features changed!")
            st.warning("Recommendation: Retrain model with fresh data.")
        else:
            st.success("✅ Model inputs stable. No retraining needed.")

except:
    st.error("⚠️ Your model not found. Run src/your_model_trainer.py first.")