<div align="center">

# ✈️ End-to-End Airline Operations Analytics Platform
### Microsoft Fabric • Apache Spark • Lakehouse • Semantic Model • Power BI

<p align="center">

![Microsoft Fabric](https://img.shields.io/badge/Microsoft_Fabric-6F2DBD?style=for-the-badge&logo=microsoft&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-0A84FF?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-F37221?style=for-the-badge&logo=apachespark&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge)
![DAX](https://img.shields.io/badge/DAX-1F77B4?style=for-the-badge)
![Lakehouse](https://img.shields.io/badge/Lakehouse-0078D4?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

</p>

---

### 🚀 End-to-End Data Engineering & Business Intelligence Project built using Microsoft Fabric

**From Synthetic Data Generation → Lakehouse → Spark Data Validation → Delta Tables → Semantic Model → Executive Power BI Dashboard**

---

</div>

# 📌 Project Overview

Modern airlines generate millions of operational records every day across multiple business systems including flight operations, passenger bookings, aircraft maintenance and weather monitoring.

This project demonstrates how these independent datasets can be transformed into a centralized analytics platform using **Microsoft Fabric's Medallion Architecture**.

Instead of building only a Power BI dashboard, this project covers the complete analytics lifecycle:

- Python-based synthetic data generation
- Bronze layer ingestion into Microsoft Fabric Lakehouse
- Data quality validation using Apache Spark notebooks
- Silver layer transformation into Delta Tables
- Gold layer semantic modeling
- Interactive Power BI executive dashboards

The final solution enables operational reporting, KPI monitoring and business decision-making using a scalable modern data platform.

---

# 🎯 Business Problem

Airline operations rely on data coming from multiple independent systems.

These datasets often contain:

- Missing values
- Duplicate records
- Invalid timestamps
- Incorrect delay values
- Inconsistent data types
- Data quality issues

Without proper validation and transformation, business reports become unreliable and decision-making suffers.

This project demonstrates how a modern data engineering pipeline can solve these challenges using Microsoft Fabric while delivering trusted business insights through Power BI.

---

# ⭐ Project Highlights

| Metric | Value |
|---------|-------|
| ✈ Flights Generated | **500,000** |
| 🎟 Bookings Generated | **300,000** |
| 🌦 Weather Records | **100,000** |
| 🔧 Maintenance Records | **20,000** |
| 🛫 Aircraft Records | **500** |
| 🌍 Airports | **150** |
| 🏗 Architecture | **Medallion (Bronze → Silver → Gold)** |
| 📊 Dashboard Pages | **4** |
| 📈 DAX Measures | **40+** |
| 🧹 Spark Validation Rules | **Multiple Business Rules** |
| 💡 Custom Tooltips | **Yes** |

---

# 🏗 Solution Architecture

```text
                         Python Dataset Generator
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │      Raw CSV Datasets        │
                    └──────────────────────────────┘
                                   │
                                   ▼
               ┌──────────────────────────────────────┐
               │      Microsoft Fabric Lakehouse      │
               │          Bronze Layer (Raw)          │
               └──────────────────────────────────────┘
                                   │
                                   ▼
                 Apache Spark Validation Notebook
          • Null Validation
          • Duplicate Detection
          • Data Type Standardization
          • Business Rule Validation
          • Error Logging
                                   │
                                   ▼
               ┌──────────────────────────────────────┐
               │      Silver Layer (Delta Tables)     │
               └──────────────────────────────────────┘
                                   │
                                   ▼
                    Semantic Model (Gold Layer)
                                   │
                                   ▼
                    Interactive Power BI Dashboard
```

---

# 🧰 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python, SQL, DAX |
| Data Engineering | Microsoft Fabric, Apache Spark, PySpark |
| Storage | OneLake, Lakehouse, Delta Tables |
| Analytics | Power BI, Semantic Model |
| Data Processing | Pandas, NumPy |
| Version Control | Git, GitHub |

---

# 📂 Dataset Overview

The project consists of six interconnected datasets that simulate real-world airline operations.

| Dataset | Description | Records |
|----------|-------------|--------:|
| Flights | Flight operations and delays | 500,000 |
| Bookings | Passenger reservations | 300,000 |
| Weather | Airport weather observations | 100,000 |
| Aircraft | Fleet information | 500 |
| Maintenance | Aircraft maintenance history | 20,000 |
| Airports | Airport master data | 150 |

---

# 📥 Project Resources

| Resource | Link |
|----------|------|
| 📦 Raw Dataset | *(Add your Google Drive Raw Dataset link here)* |
| 📊 Power BI (.pbix) | *(Add your PBIX Google Drive link here)* |
| 💻 GitHub Repository | *(Add your GitHub repository link here)* |

---
