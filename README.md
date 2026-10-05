<div align="center">

# 🔒 Security Telemetry Anomaly Detection & Threat Clustering Engine

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-sanskar00--debug-black?style=for-the-badge&logo=github)](https://github.com/sanskar00-debug/security-telemetry-anomaly-engine)

<p align="center">
  <b>Unsupervised machine learning engine for real-time authentication telemetry anomaly detection, behavioral threat profiling, and automated SOC incident alert generation.</b>
</p>

[Key Features](#-key-features) • [Architecture Flow](#-core-architecture--data-pipeline) • [Output Artifacts](#-output-artifacts)

</div>

---

## 📌 Executive Summary

Modern Security Operations Centers (SOCs) encounter extreme alert fatigue from rule-based alert engines that struggle to differentiate standard user variations from novel, low-and-slow cyberattacks. 

The **Security Telemetry Anomaly Detection & Threat Clustering Engine** is an unsupervised machine learning pipeline designed to profile multi-dimensional infrastructure telemetry. By deploying feature-standardized **K-Means clustering**, the system learns normative operational baselines directly from raw system event streams, automatically isolating high-risk outliers—such as distributed credential stuffing (brute-force) and high-throughput data exfiltration—without reliance on static, signature-based detection rules.

---

## ✨ Key Features

- **Unsupervised Anomaly Isolation:** Requires zero labeled attack data, making it resilient to zero-day and modified attack vectors.
- **Robust Feature Normalization:** Mitigates scalar dominance between discrete authentication counters (failed logins) and continuous data streams (payload transfer in MB) using `StandardScaler`.
- **Automated Behavioral Clustering:** Partitions multi-server session telemetry into statistically separate operational risk cohorts using an optimized Euclidean distance metric.
- **Tier 1 SOC Ready Output:** Automatically exports critical anomalies into an actionable incident triage file (`high_risk_security_alerts.csv`), formatted for ingestion into SIEM platforms (Splunk, Elastic, Sentinel).

---

## 📊 Core Architecture & Data Pipeline

```text
[ Raw Telemetry Ingestion ]
    │ (Failed Logins, Session Duration, Payload Velocity MB)
    ▼
[ Feature Engineering & Preprocessing ]
    │ (StandardScaler Z-Score Normalization)
    ▼
[ K-Means Threat Clustering Engine ]
    │ (Euclidean Distance Matrix / Inertia Optimization)
    ▼
[ Automated Risk Profiling & Diagnostic Triage ]
    ├──► Cluster 0: Authorized Baseline Operations (90-95%)
    ├──► Cluster 1: Brute-Force & Credential Access Spikes
    └──► Cluster 2: Anomalous Data Exfiltration Vector
            │
            ▼
[ Automated Alert Generator: high_risk_security_alerts.csv ]

```
---
## 🛠️ Technical Stack

- **Core Runtime:** Python 3.9+

- **Data Engineering:** pandas, numpy

- **Machine Learning & Feature Scaling:** scikit-learn (StandardScaler, KMeans)

- **Data Visualization & Profiling:** matplotlib, seaborn

- **Execution Environments:** CLI automation script (.py), interactive exploratory analysis (.ipynb)
---

---
## 📁 Repository Structure


security-telemetry-anomaly-engine/
├── documents/
│   └── high_risk_security_alerts.csv

├── notebook/
│   └── threat_clustering_engine.ipynb  

├── scripts/
│   └── threat_clustering_engine.py

├── requirements.txt    

├── LICENSE       

└── README.md                           

---


---

## 📄 Output Artifacts

Upon execution, the script generates a triage log under documents/high_risk_security_alerts.csv:

session_id,source_ip,failed_logins,payload_mb,assigned_cluster,risk_level.
sess_9021,192.168.1.104,24,12.4,1,HIGH_RISK_BRUTE_FORCE.
sess_4412,10.0.4.52,1,4210.8,2,CRITICAL_EXFILTRATION.
