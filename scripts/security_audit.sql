-- ====================================================================
-- TITLE: Security Telemetry Audit & Anomaly Investigation Queries
-- PURPOSE: Query K-Means generated table to prioritize high-risk threats
-- ====================================================================

USE netflix_db;

-- 1. Track high-volume data exfiltration threats sorted by data severity
SELECT 
    Failed_Logins,
    Data_Transferred_MB,
    Threat_Cluster
FROM 
    high_risk_security_alerts
WHERE 
    Threat_Cluster = 2
ORDER BY 
    Data_Transferred_MB DESC;