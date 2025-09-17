from evidently import Report
from evidently.metrics import DataDriftTable
from evidently.metrics import DataDriftPreset
import pandas as pd
import joblib
import os
import numpy as np

def detect_drift_for_your_model():
    ref_data = pd.read_csv('../data/reference_data.csv')
    current_data = ref_data.copy()
    # Simulate drift by perturbing 30% of data
    perturb_cols = current_data.columns[:2]
    for col in perturb_cols:
        noise = np.random.normal(0, 0.5, size=len(current_data))
        current_data[col] = current_data[col] + noise
    drift_report = Report(metrics=[DataDriftPreset()])
    drift_report.run(reference_data=ref_data, current_data=current_data)
    os.makedirs('../app/static', exist_ok=True)
    drift_report.save_html("../app/static/your_model_drift_report.html")
    result = drift_report.as_dict()
    dataset_drift = result['metrics'][0]['result']['dataset_drift']
    drift_share = result['metrics'][0]['result']['share_of_drifted_columns']
    print(f"⚠️ Dataset Drift Detected: {dataset_drift} | Drifted Columns: {drift_share:.2%}")
    return dataset_drift, drift_share

if __name__ == "__main__":
    detect_drift_for_your_model()