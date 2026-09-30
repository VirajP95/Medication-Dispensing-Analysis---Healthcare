import pandas as pd

full_transactions = pd.read_csv("../data/Engineered/full_transactions.csv")

#==============================Transaction volume analysis

#Most common Tx type

print(f" Most common transaction type: {full_transactions['transaction_type'].value_counts()}") 

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

















