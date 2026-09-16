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

# Merging Tx table with medication table

transaction_medication = df_transactions.merge(df_medications[['medication_id', 'medication_name', 'medication_class','medication_category','is_controlled']], on ='medication_id', how='left')

# Merging Tx table with device table

full_transactions = transaction_medication.merge(df_devices[['device_id','device_name','department',]], on='device_id', how='left')

# Merging Tx table with users table

full_transactions = full_transactions.merge(df_users[['user_id','user_name','user_role']], on='user_id', how='left')

full_transactions.columns.shape

full_transactions.tail()

#==============================Transaction volume analysis

#Most common Tx type

print(f" Most common transaction type: {df_transactions['transaction_type'].value_counts()}") 

#Tx by med class
tx_by_med_class = full_transactions.groupby('medication_class')['transaction_id'].count().sort_values(ascending=False)
tx_by_med_class

# % of Tx for controllled meds
controlled_pct = full_transactions['is_controlled'].mean() * 100 
print(f'Controlled pct: {controlled_pct: .1f}%')


#  removed medications most frequently
removed_meds = full_transactions[full_transactions['transaction_type'] == 'Remove'].groupby('medication_name')['transaction_id'].count().nlargest(10)
print(f'Most removed frequent meds: {removed_meds}')

# Peak Tx hours
peak_tx_hours = full_transactions.groupby('transaction_hours')['transaction_id'].count().sort_values(ascending=False)
print(f'Peak Transaction hours are : {peak_tx_hours}')

#Peak Tx hours
monthly_transactions = full_transactions.groupby('transaction_month')['transaction_id'].count().sort_values(ascending=False)
print(f'Monthly transaction trend: {monthly_transactions}')

#Average Tx duration by tx type

avg_Tx_duration = full_transactions.groupby('transaction_type')['transaction_duration_sec'].mean().round(1).sort_values(ascending=False)
print('Average TX duration by type: avg_Tx_duration: (seconds)')
print(avg_Tx_duration)

#Department with highhest Tx volume
department_Tx = full_transactions.groupby('department')['transaction_id'].count().sort_values(ascending=False)
print(f'Department with highest Tx volume: {department_Tx}')

















