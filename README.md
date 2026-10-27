Healthcare Medication Dispensing Analysis

An end-to-end data analysis project simulating real-world Pyxis medication dispensing system data across a hospital environment. The project covers data cleaning, exploratory analysis, SQL querying, and Power BI reporting — built as a portfolio project for a healthcare data analyst role.

Project Overview

Item	Detail
Dataset	Mock Pyxis dispensing data — 6 tables, ~3,000+ rows
Tools	Python (pandas, matplotlib, seaborn), MSSQL, Power BI
Topics	Transaction analysis, compliance monitoring, device usage, inventory management
Repository Structure
├── MSSQL/
│   ├── Created_Tables&Columns.sql     # Table creation scripts
│   └── SQLAnalysis.sql                # All SQL analysis queries
│
├── PowerBI/                           # Power BI dashboard (.pbix)
│
├── scripts/
│   ├── 01_EDA.py                      # Exploratory data analysis
│   ├── 02_Clean_Data.py               # Data cleaning across all 6 tables
│   ├── 03_Transform_data.py           # Feature engineering and merges
│   ├── 04_Transaction_Analysis.py     # Topic 1 — transaction patterns
│   ├── 05_ComplianceAnalysis.py       # Topic 2 — override & discrepancy analysis
│   ├── 06_Device&inventory_Analysis.py# Topic 3 & 4 — device usage and inventory
│   ├── 07_Importing_Data_into_SQL.py  # Load clean data into MSSQL
│   └── 08_Visualizations.py           # Matplotlib/Seaborn charts
│
├── sql/                               # Additional SQL scripts
├── Project_Findings.docx              # Full findings document with recommendations
├── requirements.txt
└── README.md
Dataset

Six tables modelling a hospital Pyxis dispensing system:

Table	Rows	Description
fact_transactions	1,505	Every medication dispensing event
dim_devices	40	Pyxis devices across 16 departments
dim_medications	50	Medication details — class, category, controlled status
dim_users	28	Staff — RNs, Pharmacists, Anesthesiologists
dim_patients	300	Patient visit information
dim_inventory	1,141	Medication stock levels per device and drawer

The dataset contained intentionally planted data quality issues (missing values, casing inconsistencies, negative quantities, duplicates, future dates) that were identified and resolved during cleaning.

Analysis Topics
1. Transaction Analysis
Remove is the most common transaction type, reflecting standard dispensing workflow
ICU has the highest transaction volume across all departments
Top dispensed medications: Piperacillin-Tazobactam 3.375g, Vancomycin 1g, Lactated Ringers 1L
Peak transaction hours: 7 AM, 8 AM, and 2 PM

2. Override & Compliance Analysis
Override transactions are concentrated in PACU, ICU, and Pediatrics — high-acuity departments
Controlled substances account for a disproportionate share of overrides (100 vs 44 non-controlled)
Most overridden medications: Meperidine 50mg/mL, Lorazepam 2mg/mL, Hydromorphone 2mg
100% witness compliance on all controlled medication Return/Waste transactions — zero breaches

3. Discrepancy Analysis
Overall discrepancy rate: 2.9% (42 out of 1,460 transactions)
Controlled medication discrepancy rate: 3.93%
ICU-Station-3 and PACU-Station-1 appear across both high-override and high-discrepancy categories

4. Inventory Analysis
300 medication slots flagged as needing restock
Most understocked devices: TELE-Station-1, ER2-Station-3, ER1-Station-1
Emergency Room 2 has both low stock levels and elevated override rates — indicating a direct link between stock shortages and bypass behaviour
