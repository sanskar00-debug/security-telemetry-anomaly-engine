import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Simulate Meshed Network Log Data
np.random.seed(42)
n_samples = 500

# Normal Employee Profile Behavior (Cluster 0)
failed_logins_normal = np.random.poisson(lam=1, size=450)
data_volume_normal = np.random.normal(loc=50, scale=15, size=450) # MBs

# Malicious / Brute-Force / Data Exfiltration Behavior (Cluster 1 & 2 anomalies)
failed_logins_threat = np.random.randint(low=8, high=25, size=50)
data_volume_threat = np.random.normal(loc=450, scale=100, size=50) # Heavy Exfiltration

# Merge Telemetry into a Single Security DataFrame
df = pd.DataFrame({
    'Failed_Logins': np.concatenate([failed_logins_normal, failed_logins_threat]),
    'Data_Transferred_MB': np.concatenate([data_volume_normal, data_volume_threat])
})

# Shuffle logs to simulate an active real-world stream
df = df.sample(frac=1).reset_index(drop=True)
print("--- Messy Telemetry Stream Loaded ---")
print(df.head())

# 2. Preprocessing & Feature Scaling (Crucial for Distance-based K-Means)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# 3. Initialize & Train the Anomaly Threat Clustering Engine
# We choose 3 clusters: 1 for baseline normal behavior, 2 variations of risk profiles
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Threat_Cluster'] = kmeans.fit_predict(scaled_features)

# 4. Profile the Risk Output Behavior
print("\n--- Threat Cluster Behavioral Summary ---")
cluster_profile = df.groupby('Threat_Cluster').mean()
print(cluster_profile)

# Identify the highest risk cluster programmatically
high_risk_cluster = cluster_profile['Failed_Logins'].idxmax()
print(f"\n⚠️ Action Required: Cluster {high_risk_cluster} flagged as HIGH RISK Anomaly.")

# 5. Export Suspicious IP Log Alerts for SOC Analysts
malicious_alerts = df[df['Threat_Cluster'] == high_risk_cluster]
malicious_alerts.to_csv("high_risk_security_alerts.csv", index=False)
print(f"🔒 Isolated {len(malicious_alerts)} high-risk anomalies to 'high_risk_security_alerts.csv'")
