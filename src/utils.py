import smtplib
from email.mime.text import MIMEText
import requests

def send_slack_alert(message, webhook_url="https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"):
    payload = {"text": f"🚨 ALERT: {message}"}
    try:
        requests.post(webhook_url, json=payload, timeout=5)
        print("✅ Slack alert sent.")
    except:
        print("❌ Slack alert failed.")

def send_email_alert(subject, body, to_email="your-email@gmail.com"):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "hackathon-alert@yourproject.com"
        msg['To'] = to_email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login("your-email@gmail.com", "your-app-password")
            server.send_message(msg)
        print("✅ Email alert sent.")
    except Exception as e:
        print(f"❌ Email alert failed: {e}")

# Example: send_slack_alert("Model drift detected! 40% features drifted.")