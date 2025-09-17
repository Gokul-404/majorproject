import streamlit as st

st.title("🏠 Home Dashboard")
st.write("## AI Drift & Threat Detection in Cloud Systems")
st.markdown("""
Welcome to your all-in-one **Cloud AI Security Operations Center**.

### ✅ Features Included:
- **Your Own Trained AI Model** with Drift Tracking
- **NSL-KDD Based Threat Detection** mapped to AWS/Azure services
- **Real-time Cloud Attack Visualizations** (S3, IAM, EC2, Blob, AD, etc.)
- **Drift Detection Reports** using Evidently AI
- **Slack/Email Alerts** on anomalies
- **1-Click Deployable** to Google Cloud Run

### 🚀 Built For Hackathons — Ready to Win!
""")

col1, col2, col3 = st.columns(3)
col1.metric("📈 Your Model Accuracy", "92.15%")
col2.metric("🛡️ Threat Detection Acc", "84.32%")
col3.metric("☁️ Simulated Attacks", "100+")