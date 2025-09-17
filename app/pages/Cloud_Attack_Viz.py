import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("☁️ Cloud Attack Simulation (AWS & Azure)")

tab1, tab2 = st.tabs(["AWS Attacks", "Azure Attacks"])

aws_df = pd.read_csv('../data/aws_attacks.csv')
azure_df = pd.read_csv('../data/azure_attacks.csv')

with tab1:
    st.subheader("AWS Attack Timeline")
    fig = px.scatter(aws_df,
                    x='timestamp',
                    y='target_service',
                    color='severity',
                    symbol='status',
                    hover_data=['attack_type', 'source_ip'],
                    title="AWS Attacks by Service & Severity")
    st.plotly_chart(fig, use_container_width=True)
    
    st.metric("🔴 Critical AWS Incidents", len(aws_df[aws_df['severity']=='Critical']))

with tab2:
    st.subheader("Azure Attack Severity Radar")
    severity_counts = azure_df['severity'].value_counts()
    fig2 = go.Figure(data=go.Scatterpolar(
        r=severity_counts.values,
        theta=severity_counts.index,
        fill='toself',
        name='Azure'
    ))
    fig2.update_layout(polar=dict(radialaxis=dict(visible=True)), title="Azure Attack Severity")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("🔐 Simulated Attack Flow")
attack_flow = """
1. Attacker → Scans Public S3 Buckets → Finds Misconfigured Bucket → Downloads PII Data → Exfiltrates to C2 Server
2. Attacker → Brute Forces Azure AD → Gains User Access → Escalates Privileges → Dumps CosmosDB
"""
st.code(attack_flow, language='text')
st.image("https://via.placeholder.com/800x200?text=Animated+Attack+Flow+GIF+Here", caption="Simulated Cloud Attack Chain")