import pandas as pd
from sqlalchemy import create_engine

# ══════════════════════════════════════════════
# CONNECT TO SQL SERVER
# ══════════════════════════════════════════════
engine = create_engine(
    'mssql+pyodbc://VIRAJ_PC\\SQLEXPRESS/healthcare_analysis'
    '?driver=ODBC+Driver+17+for+SQL+Server'
    '&trusted_connection=yes'
)

# ══════════════════════════════════════════════
# LOAD ALL CLEAN TABLES
# ══════════════════════════════════════════════
tables = {
    'fact_transactions': '../data/cleaned/fact_transactions.csv',
    'dim_medications':   '../data/cleaned/dim_medications.csv',
    'dim_devices':       '../data/cleaned/dim_devices.csv',
    'dim_users':         '../data/cleaned/dim_users.csv',
    'dim_patients':      '../data/cleaned/dim_patients.csv',
    'dim_inventory':     '../data/cleaned/dim_inventory.csv',
}

for table_name, file_path in tables.items():
    df = pd.read_csv(file_path)
    df.to_sql(
        table_name,
        engine,
        if_exists='replace',  # drops and recreates table
        index=False
    )
    print(f"✓ {table_name}:  {len(df)} rows loaded")

print("\nAll tables loaded successfully!")