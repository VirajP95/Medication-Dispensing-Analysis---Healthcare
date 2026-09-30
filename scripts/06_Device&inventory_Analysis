import pandas as pd

full_transactions = pd.read_csv("../data/Engineered/full_transactions.csv")

df_inventory = pd.read_csv("../data/cleaned/dim_inventory.csv")


# ======================================== Device Usgae Analysis =====================================

# Devices with highest total transaction volume

device_Tx = full_transactions.groupby('device_name')['transaction_id'].count().nlargest(10)
print(f'Devices with highest transaction volume are: {device_Tx}')

# Dept with highest controlled meds consumption

controlled_consumption = full_transactions[full_transactions['is_controlled'] == True].groupby('department')['transaction_id'].count().sort_values(ascending=False)
print(f'Department with highest comsmption of controlled meds are: {controlled_consumption}')

# Devices with highest discrepancy count 

devices_discrepancy_count = full_transactions[full_transactions['discrepancy_flag'] == 1].groupby('device_name')['transaction_id'].count().nlargest(10)
print(f'Devices with highest discrepancy count are :{devices_discrepancy_count}')

#Average transaction duration per department

tx_avg_duration = full_transactions.groupby('department')['transaction_duration_sec'].mean().round(1).sort_values(ascending=False)
print(f'Average transaction duration per department is : {tx_avg_duration}')

# Which drawerd are accessed most across all devices

device_drawer_access = full_transactions.groupby('drawer_number')['transaction_id'].count().sort_values(ascending=False)
print(f'Drawers that are accessed most across all devices are {device_drawer_access}')

# ======================================== Inventory Analysis =====================================

df_inventory.tail()

# Meds that need refill now

needs_refill= df_inventory[df_inventory['needs_restock'] == 1]
meds_restock = needs_refill.groupby('medication_name')['inventory_id'].count().sort_values(ascending=False)
print(f'Count of meds that need restock: {len(needs_refill)}')
print(f'Unqiue Medications that need restock: {needs_refill['medication_name'].nunique()}')
print(f'\nMedications that need restock across most device locations:')
print(meds_restock.head(10))

# Devices that are currently understocked

device_stock = df_inventory[df_inventory['needs_restock'] == 1].groupby('device_name')['inventory_id'].count().nlargest(10)

print(f'Total devices with understocked items: {df_inventory[df_inventory['needs_restock'] == 1]['device_name'].nunique()}')
print('\nTop 10 most understocked devices Devices with understocked items:')
print(device_stock)


# Medications that are overstocked across devices

overstocked= df_inventory[df_inventory['current_quantity'] > df_inventory['par_level']]

meds_overstock = overstocked.groupby(['medication_name','device_name'])['inventory_id'].count().nlargest(10)
print(meds_overstock)

#Stock level - controlled vs non-controlled 

stock_level = df_inventory.groupby('is_controlled')['current_quantity'].sum()
print(stock_level)

# Department with lowest average stock level

dept_stock = df_inventory.groupby('department')['current_quantity'].mean().round(2).nsmallest(10)
dept_stock
















