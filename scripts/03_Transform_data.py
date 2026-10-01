import pandas as pd

df_transactions = pd.read_csv('../data/cleaned/fact_transactions.csv')

df_medications = pd.read_csv('../data/cleaned/dim_medications.csv')

df_devices = pd.read_csv('../data/cleaned/dim_devices.csv')

df_users = pd.read_csv('../data/cleaned/dim_users.csv')

df_inventory = pd.read_csv('../data/cleaned/dim_inventory.csv')

df_patients = pd.read_csv('../data/cleaned/dim_patients.csv')

df_transactions.tail()
df_medications.tail()
df_devices.tail()
df_users.tail()
df_inventory.tail()
df_patients.tail()


# Merging Tx table with medication table

transaction_medication = df_transactions.merge(df_medications[['medication_id', 'medication_name', 'medication_class','medication_category','is_controlled']], on ='medication_id', how='left')

# Merging Tx table with device table

full_transactions = transaction_medication.merge(df_devices[['device_id','device_name','department']], on='device_id', how='left')

# Merging Tx table with users table

full_transactions = full_transactions.merge(df_users[['user_id','user_name','user_role']], on='user_id', how='left')

# Meging TX table with patients table

full_transactions = full_transactions.merge(df_patients[['patient_id', 'patient_name','patient_type','visit_status','visit_date']], on='patient_id', how='left')


# Converting datime columns to datetime
full_transactions['transaction_datetime'] = pd.to_datetime(full_transactions['transaction_datetime'])

full_transactions['transaction_month'] = full_transactions['transaction_datetime'].dt.month

full_transactions['transaction_hours'] = full_transactions['transaction_datetime'].dt.hour


full_transactions.tail()

full_transactions.to_csv('../data/Engineered/full_transactions.csv', index=False)

