# Security Telemetry Anomaly Detection & Threat Clustering Engine 🔒

## 📌 Project Overview
This repository contains a production-ready, data-driven security engine designed to identify network infrastructure threats and anomalous user behavior. Using unsupervised machine learning (**K-Means Clustering**), the pipeline processes raw authentication telemetry logs, establishes normal system behavioral baselines, and isolates high-risk anomalies (such as brute-force access profiles and data exfiltration attempts) without requiring predefined manual signatures.

The project isolates messy infrastructure telemetry feeds, calculates distance-based threat metrics, and automatically outputs a triage-ready tracking log (`high_risk_security_alerts.csv`) tailored for Tier 1 Security Operations Center (SOC) review.

## 🛠️ Technical Stack & Tools
- **Language:** ![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54) **Python 3.x**.
- **Data Engineering & Preprocessing:** ![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white), ![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white), ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white).
- **Machine Learning Engine:** Scikit-Learn (K-Means Clustering)
- **Data Pipeline Analytics:** Integrated Relational Database / Flat CSV Exports

## 📊 Core Architecture Flow
1. **Telemetry Ingestion:** Simulates multi-server event logs tracking key operational security variables: failed login counts and payload volume velocity (MB).
2. **Feature Scaler Matrix:** Utilizes Z-score standardization (`StandardScaler`) to neutralize magnitude differences between access frequency constraints and raw data payloads.
3. **Behavioral Clustering Engine:** Deploys a distance-optimized K-Means model to partition log sessions into distinct tactical risk categories.
4. **Programmatic Triage:** Evaluates cluster centers to isolate the highest-risk data vectors and auto-generates a SOC incident alert file.

## 🚀 How to Run the Threat Engine
Ensure you have the required packages installed:
```bash
pip install pandas numpy scikit-learn matplotlib
```

Clone the repository and execute the security diagnostics engine:
```bash
git clone https://github.com
cd security-telemetry-anomaly-engine
python threat_clustering_engine.py
```

## 📈 Security Insights & Cluster Profiling
When executed, the engine automatically profiles network behavior into three clean diagnostic segments:
- **Cluster 0 (Baseline Operations):** Low failed login frequencies, standard data transfer volumes. Represents legitimate, authorized corporate usage patterns.
- **Cluster 1 (Brute-Force Vector):** Spikes in sequential access failure events with standard data usage. Indicates probable credential-stuffing or dictionary attacks.
- **Cluster 2 (Exfiltration Vector):** High data volume payloads paired with anomalous system events. Indicates potential insider threats or compromised service accounts moving enterprise assets out of the network footprint.

## 📂 Expected Output Artifacts
- `high_risk_security_alerts.csv`: A highly structured, filtered log file listing every session identifier flagged as an infrastructure anomaly for automated ingestion into a SIEM platform.
