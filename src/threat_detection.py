import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

col_names = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land",
    "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised",
    "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells",
    "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login",
    "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate",
    "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
    "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "attack_type", "difficulty_level"
]

def load_and_preprocess_nsl_kdd():
    print("📂 Loading NSL-KDD dataset...")
    train_df = pd.read_csv('../data/nsl-kdd/KDDTrain+.txt', names=col_names, header=None)
    test_df = pd.read_csv('../data/nsl-kdd/KDDTest+.txt', names=col_names, header=None)
    train_df.drop('difficulty_level', axis=1, inplace=True)
    test_df.drop('difficulty_level', axis=1, inplace=True)
    le_protocol = LabelEncoder()
    le_service = LabelEncoder()
    le_flag = LabelEncoder()
    le_attack = LabelEncoder()
    for df in [train_df, test_df]:
        df['protocol_type'] = le_protocol.fit_transform(df['protocol_type'])
        df['service'] = le_service.fit_transform(df['service'])
        df['flag'] = le_flag.fit_transform(df['flag'])
        df['attack_type'] = le_attack.fit_transform(df['attack_type'])
    os.makedirs('../models', exist_ok=True)
    joblib.dump(le_attack, '../models/le_attack.pkl')
    X_train = train_df.drop('attack_type', axis=1)
    y_train = train_df['attack_type']
    X_test = test_df.drop('attack_type', axis=1)
    y_test = test_df['attack_type']
    return X_train, X_test, y_train, y_test, le_attack

def train_threat_model():
    X_train, X_test, y_train, y_test, le_attack = load_and_preprocess_nsl_kdd()
    print("🧠 Training Threat Detection Model (Random Forest)...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Threat Model Trained! Test Accuracy: {acc:.4f}")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=le_attack.classes_))
    joblib.dump(model, '../models/threat_model.pkl')
    print("💾 Threat model saved.")
    return model, X_test, y_test

if __name__ == "__main__":
    train_threat_model()