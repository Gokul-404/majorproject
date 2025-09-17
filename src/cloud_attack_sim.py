import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def simulate_aws_attacks(n_attacks=50):
    attack_types = ["S3_Bucket_Enumeration", "IAM_Credential_Theft", "EC2_Port_Scan", "Lambda_Data_Exfil", "RDS_SQL_Injection"]
    data = {
        'timestamp': [datetime.now() - timedelta(minutes=np.random.randint(1, 60)) for _ in range(n_attacks)],
        'attack_type': np.random.choice(attack_types, n_attacks),
        'source_ip': [f"192.168.{np.random.randint(1,255)}.{np.random.randint(1,255)}" for _ in range(n_attacks)],
        'target_service': np.random.choice(['S3', 'EC2', 'IAM', 'Lambda', 'RDS'], n_attacks),
        'severity': np.random.choice(['Low', 'Medium', 'High', 'Critical'], n_attacks, p=[0.4, 0.3, 0.2, 0.1]),
        'status': np.random.choice(['Blocked', 'Alerted', 'Compromised'], n_attacks, p=[0.7, 0.2, 0.1])
    }
    return pd.DataFrame(data)

def simulate_azure_attacks(n_attacks=50):
    attack_types = ["Blob_Storage_Leak", "Azure_AD_Brute_Force", "VMSS_Port_Scan", "Function_App_RCE", "CosmosDB_NoSQL_Injection"]
    data = {
        'timestamp': [datetime.now() - timedelta(minutes=np.random.randint(1, 60)) for _ in range(n_attacks)],
        'attack_type': np.random.choice(attack_types, n_attacks),
        'source_ip': [f"10.{np.random.randint(1,255)}.{np.random.randint(1,255)}.{np.random.randint(1,255)}" for _ in range(n_attacks)],
        'target_service': np.random.choice(['Blob Storage', 'Azure AD', 'VMSS', 'Function App', 'CosmosDB'], n_attacks),
        'severity': np.random.choice(['Low', 'Medium', 'High', 'Critical'], n_attacks, p=[0.4, 0.3, 0.2, 0.1]),
        'status': np.random.choice(['Blocked', 'Alerted', 'Compromised'], n_attacks, p=[0.7, 0.2, 0.1])
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    os.makedirs('../data', exist_ok=True)
    aws_attacks = simulate_aws_attacks()
    azure_attacks = simulate_azure_attacks()
    aws_attacks.to_csv('../data/aws_attacks.csv', index=False)
    azure_attacks.to_csv('../data/azure_attacks.csv', index=False)
    print("☁️ Simulated AWS & Azure attack data saved to /data/")