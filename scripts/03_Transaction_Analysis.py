import pandas as pd

df_transactions = pd.read_csv('../data/cleaned/fact_transactions.csv')

df_medications = pd.read_csv('../data/cleaned/dim_medications.csv')

df_devices = pd.read_csv('../data/cleaned/dim_devices.csv')

df_users = pd.read_csv('../data/cleaned/dim_users.csv')

df_transactions.tail()
df_medications.tail()
df_devices.tail()
df_users.tail()

df_transactions['transaction_datetime'] = pd.to_datetime(df_transactions['transaction_datetime'])

df_transactions['transaction_month'] = df_transactions['transaction_datetime'].dt.month

df_transactions['transaction_hours'] = df_transactions['transaction_datetime'].dt.hour

# Merging transaction table with medication table

medication_transactions = df_transactions.merge(df_medications[['medication_id', 'medication_name', 'medication_class','medication_category','is_controlled']], on ='medication_id', how='left')

# Merging transactions table with device table

device_transactions = df_transactions.merge(df_devices[['device_id','device_name','department',]], on='device_id', how='left')

# Merging transactions table with users table

user_transactions = df_transactions.merge(df_users[['user_id','user_name','user_role']], on='user_id', how='left')

# Transaction volume analysis







