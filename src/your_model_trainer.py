import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def generate_phishing_data(n_samples=10000):
    np.random.seed(42)
    data = {
        'url_length': np.random.randint(10, 200, n_samples),
        'has_ip': np.random.choice([0, 1], n_samples),
        'has_at': np.random.choice([0, 1], n_samples),
        'redirect_count': np.random.randint(0, 5, n_samples),
        'is_phishing': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    }
    return pd.DataFrame(data)

def train_your_model():
    print("🧠 Training Your Custom AI Model (Phishing URL Classifier)...")
    df = generate_phishing_data()
    X = df.drop('is_phishing', axis=1)
    y = df['is_phishing']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model Trained! Test Accuracy: {acc:.4f}")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred))
    os.makedirs('../models', exist_ok=True)
    os.makedirs('../data', exist_ok=True)
    joblib.dump(model, '../models/your_ai_model.pkl')
    X_train.to_csv('../data/reference_data.csv', index=False)
    print("💾 Model & reference data saved.")
    return model, X_test, y_test

if __name__ == "__main__":
    train_your_model()