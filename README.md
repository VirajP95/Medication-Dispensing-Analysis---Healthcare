# Healthcare Medication Dispensing Analysis (Pyxis)

An end-to-end data analysis project using **mock** Pyxis medication dispensing data from a simulated hospital. It covers data cleaning, exploratory analysis, SQL querying, and Power BI reporting. All patient and staff data is synthetic.


This project is for the Director of Pharmacy or Pharmacy teams to understand Medication Dispensing across all devices. It answers business questions pertaining to number of medications that were dispensed, Override & Discrepancies that occurred during transactions and also includes Device and Inventory information which will help pharmacy staff to have a better understanding of transaction workflows across several devices supported by visual charts and in depth analysis.

## Business Questions
1. Which medications are removed most frequently across all devices?
2. Which transaction type (Remove/Waste/Override/Refill/Return) has the highest volume?
3. Which medication type has the highest number of overrides? 

## Dashboard
<img width="1268" height="712" alt="Transaction analysis page" src="https://github.com/user-attachments/assets/3d68209e-fe9e-4bce-9d10-55dee4b3e225" /> 


First page in this report showcases Transaction visuals which gives a better understanding of Medication Dispensing across the hospital.

<img width="1220" height="684" alt="image" src="https://github.com/user-attachments/assets/11c72180-d84f-4692-af3b-0e13aac85eed" />



Second page highlights Override and Discrepancy analysis in addition to users who contributed to override transactions.



## Project Overview

| Item | Detail |
|---|---|
| Dataset | Mock Pyxis dispensing data: 6 tables, ~3,000 rows |
| Tools | Python (pandas, matplotlib, seaborn), SQL Server, Power BI |
| Topics | Transaction analysis, compliance monitoring, device usage, inventory management |

## Dataset

| Table | Rows (raw → cleaned) | Description |
|---|---|---|
| fact_transactions | 1,505 → 1,460 | Every medication dispensing event |
| dim_devices | 40 | Pyxis devices across 16 departments |
| dim_medications | 50 | Medication details: class, category, controlled status |
| dim_users | 29 → 28 | Staff: RNs, pharmacists, anesthesiologists |
| dim_patients | 300 | Patient visit information |
| dim_inventory | 1,141 → 1,136 | Medication stock levels per device and drawer |

The dataset contained intentionally planted data quality issues (missing values, inconsistent casing and department names, negative quantities, duplicates, future dates), which were identified and resolved during cleaning.

## Key Findings

### 1. Transaction Analysis
- Remove is the most common transaction type, reflecting standard dispensing workflow
- ICU and MedSurg have the highest transaction volume (139 transactions each).
- Top dispensed medications: Piperacillin-Tazobactam 3.375g, Vancomycin 1g, Lactated Ringers 1L
- Peak transaction hours: 7 AM, 8 AM, and 2 PM

### 2. Override & Compliance Analysis
- Override transactions are concentrated in PACU, ICU, and Pediatrics, which are high-acuity departments
- Controlled substances account for a disproportionate share of overrides (100 vs 44 non-controlled)
- Most overridden medications: Meperidine 50mg/mL, Lorazepam 2mg/mL, Hydromorphone 2mg
- 100% witness compliance on all controlled medication Return/Waste transactions, with zero breaches

### 3. Discrepancy Analysis
- Overall discrepancy rate: 2.9% (42 of 1,460 transactions)
- Controlled medication discrepancy rate: 3.93%
- ICU-Station-3 and PACU-Station-1 appear in both the high-override and high-discrepancy lists

### 4. Inventory Analysis
- 300 medication slots flagged as needing restock
- Most understocked devices: TELE-Station-1, ER2-Station-3, ER1-Station-1
- Emergency Room 2 has both low stock levels and elevated override rates, indicating a direct link between stock shortages and bypass behaviour

## Repository Structure
```
├── MSSQL/
│   ├── Created_Tables&Columns.sql     # Table creation scripts
│   └── SQLAnalysis.sql                # SQL analysis queries
├── PowerBI/                           # Power BI dashboard (.pbix)
├── data/
│   ├── raw/                           # Original mock data
│   ├── cleaned/                       # Output of 02_Clean_Data.py
│   └── Engineered/                    # Output of 03_Transform_data.py
├── scripts/
│   ├── 01_EDA.py                      # Exploratory data analysis
│   ├── 02_Clean_Data.py               # Data cleaning across all 6 tables
│   ├── 03_Transform_data.py           # Merges and time features
│   ├── 04_Transaction_Analysis.py     # Transaction patterns
│   ├── 05_ComplianceAnalysis.py       # Override & discrepancy analysis
│   ├── 06_Device&inventory_Analysis.py # Device usage and inventory
│   ├── 07_Importing_Data_into_SQL.py  # Load clean data into SQL Server
│   └── 08_Visualizations.py           # Matplotlib/Seaborn charts
├── Project_Findings.docx              # Full findings with recommendations
├── requirements.txt
└── README.md
```

## How to Run
1. `pip install -r requirements.txt`
2. From the `scripts` folder, run the scripts in order: `python 01_EDA.py`, `python 02_Clean_Data.py`, and so on
3. Open `PowerBI/Medication Dispensing Dashboard.pbix` and click Refresh
