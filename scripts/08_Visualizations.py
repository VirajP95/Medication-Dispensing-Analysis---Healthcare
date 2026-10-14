import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

full_transactions = pd.read_csv("../data/Engineered/full_transactions.csv", )

df_inventory_clean = pd.read_csv("../data/cleaned/dim_inventory.csv")

df_devices_clean = pd.read_csv("../data/cleaned/dim_devices.csv")

full_transactions.tail()

# ==============================Transaction Charts=========================

# Bar Chart - Transaction volume by Type 

tx_counts = full_transactions.groupby('transaction_type')['transaction_id'].count()
tx_counts.plot.bar(color='steelblue')
plt.title('Transaction Volume By Type')
plt.xlabel('Transaction Months')
plt.xticks(ticks= [1,2,3,4,5,6], labels= ['Jan','Feb', 'March', 'April', 'May','June'])
plt.ylabel('Transactions')

# Line Chart - Montly transaction trend

tx_trend = full_transactions.groupby('transaction_month')['transaction_id'].count()
tx_trend.plot.line()
plt.title('Monthly Transaction trend')
plt.xlabel("Transaction Month")
plt.ylabel("Transactions")
plt.xticks(ticks= [1,2,3,4,5,6], labels= ['Jan','Feb', 'March', 'April', 'May', 'June'])
plt.tight_layout()

# Stacked bar chart - Transaction type by Department

tx_by_dept = full_transactions.groupby(['department','transaction_type']).size().unstack(fill_value=0)
tx_by_dept.plot.bar(stacked=True, figsize=(14,6))
plt.title("Transaction types by department")
plt.xlabel('Departments')
plt.ylabel('Number of transactions')

# =================================Complaince charts=============================

# Bar Chart - Top 10 users by override count

users_cnt = full_transactions[full_transactions['transaction_type'] == 'Override'].groupby('user_name')['transaction_id'].count().nlargest(10)
users_cnt.plot.bar()
plt.title("Top 10 users by Override Count")
plt.xlabel("User Names")
plt.ylabel("Number of Transactions")


full_transactions['is_override'] = (full_transactions['transaction_type'] == 'Override')

# Top 10 users by override rate
override_by_user = (full_transactions
    .groupby(['user_name'])['is_override']
    .mean() * 100
).round(1).nlargest(10)

override_by_user.plot.barh(color='crimson', figsize=(15, 6))
plt.title('Top 10 Users by Override Rate')
plt.xlabel('Override Rate (%)')
plt.ylabel('User Name')

# Bar Chart - Discrepancies by medication class

disc_med_class = full_transactions[full_transactions['discrepancy_flag'] == 1].groupby(['medication_class'])['transaction_id'].count()

disc_med_class.plot.bar(color='darkred')
plt.title("Discrepancies by medication class")
plt.xlabel('Medication Class')
plt.xticks(ticks=[0.0,1.0,2.0,3.0,4.0,5.0])
plt.ylabel('Number of transactions')


# ==============================Device & Inventory Charts ==================================

# Top 10 devices by Volume 

top_devices = full_transactions.groupby('device_name')['transaction_id'].count().nlargest(10).sort_values(ascending=False)

top_devices.plot.barh()
plt.title('Top 10 Devices by Volume')
plt.xlabel('Number of Transactions ')
plt.ylabel('Device Names')
plt.xlim(0, top_devices.max() + 10) 

# Pie Chart - Controlled vs Non-Controlled 

control_cnts = full_transactions['is_controlled'].value_counts()
control_cnts.index = ['Non-Controlled','Controlled']
control_cnts.plot.pie(autopct='%1.1f%%')
plt.show()

# Bar Chart: Departments with most restocking

restock = df_inventory_clean[df_inventory_clean['needs_restock'] == 1]

restock_dept = restock.merge(df_devices_clean[['device_id']], on="device_id")

restock_dept.groupby('department')['inventory_id'].count().sort_values().plot.barh()
plt.title("Items needing restock by department")
plt.show()
plt.fig
print

print(restock_dept.shape)
print(restock_dept.columns.to_list())