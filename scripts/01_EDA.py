import pandas as pd


df_transactions= pd.read_csv('../data/raw/fact_transactions.csv')

df_medications = pd.read_csv('../data/raw/dim_medications.csv')

df_devices = pd.read_csv('../data/raw/dim_devices.csv')

df_inventory = pd.read_csv('../data/raw/dim_inventory.csv')

df_patients = pd.read_csv('../data/raw/dim_patients.csv')

df_users = pd.read_csv('../data/raw/dim_users.csv')


df_transactions.shape
df_transactions.info()


#-------------------------- EDA 1 — FACT_TRANSACTIONS ------------------------------

df_transactions.tail()

df_transactions.isnull().sum()

df_transactions.duplicated(subset=['transaction_id']).sum()
print(f"Unique Transaction ids: {df_transactions['transaction_id'].nunique()}")

df_transactions['transaction_type'].value_counts()


#------- Checking for 6 digits order number

valid_orders = df_transactions['order_number'].dropna()
print(f"Less than 6 chars: {(valid_orders.str.len()<6).sum()}")
print(f"More than 6 chars: {(valid_orders.str.len()>6).sum()}")
print(f"Exactly six chars: {(valid_orders.str.len()==6).sum()}")


#----- Checking quantity column for negative values 

quantity_check = df_transactions[df_transactions['quantity'] < 0]
print(f"Total negative rows: {len(quantity_check)}") 

df_transactions['drawer_number'].value_counts()

df_transactions['discrepancy_flag'].value_counts()


print("============Transaction Date EDA============")

converted = pd.to_datetime(df_transactions['transaction_datetime'], errors='coerce')

#Type
print(f'Datatype: {df_transactions['transaction_datetime'].dtype}')

#Missing
missing = df_transactions[df_transactions['transaction_datetime'].isnull()]
print(f'Missing Dates: {len(missing)}')

#Unparseable
invalid = df_transactions[converted.isnull() & df_transactions['transaction_datetime'].notna()]
print(f'Invalid Dates: {len(invalid)}')

#Future Dates
future = df_transactions[converted > '2024-06-30']
print(f'Future Dates: {len(future)}')

#Range
print(f'Mimimum: {converted.min()}')
print(f'Maximum: {converted.max()}')

#Monthly Distribution
print(f'Monthly Transactions:{converted.dt.month.value_counts().sort_index()}')


#-------------------------- EDA 2 — DIM_Medications ------------------------------

df_medications.tail()

df_medications.isnull().sum()

#Checking unique values for is_controlled and require_witness fields
df_medications.groupby(['is_controlled','requires_witness']).size()  

df_medications['medication_class'].value_counts()

df_medications['medication_category'].unique()


#Spacing check
leading_trailing_space = df_medications[df_medications['medication_name' ] != df_medications['medication_name'].str.strip()]
print(leading_trailing_space)

medication_double_space = df_medications[df_medications['medication_name'].str.contains('  ')]
print(medication_double_space)

#-------------------------- EDA 3 — DIM_Users ------------------------------


df_users.tail()

df_users.isnull().sum()

#--------- 
user_name_space_check = df_users[df_users['user_name'] != df_users['user_name'].str.strip()]
print(user_name_space_check)

user_double_space = df_users[df_users['user_name'].str.contains('  ')]
print(user_double_space)

df_users['user_role'].unique()

df_users[df_users['areas_assigned'].isnull()]

Duplicate_users = df_users[df_users["user_name"].duplicated()]
Duplicate_users

#-------------------------- EDA 4 — DIM_Patients ------------------------------

df_patients.tail(5)

patients_null_values = df_patients.isnull().sum()
patients_null_values

print(f"Duplicate Patient IDs: {df_patients.duplicated(subset=['patient_id']).sum()}")

df_patients["patient_type"].value_counts()

df_patients["visit_status"].value_counts()

print("======VISIT DATE EDA=========")
converted = pd.to_datetime(df_patients['visit_date'], errors='coerce')

#Type
print(f" Data Type: {df_patients['visit_date'].dtype}")

#Missing
print(f"Missing date values : {df_patients['visit_date'].isnull().sum()}")


#Unparseable
invalid = df_patients[converted.isnull() & df_patients['visit_date'].notna()]
print(f'Invalid dates: {len(invalid)}')


#Future Dates
future = df_patients[converted > '2024-06-30']
print(f'Future Dates: {len(future)}')

#Range
print(f'Minimum: {converted.min()}')
print(f'Maxmimum: {converted.max()}')

#Monthly Distriubution
print(f'\nMonthly Distribution:')
print(converted.dt.month.value_counts().sort_index())

#-------------------------- EDA 4 — DIM_Inventory ------------------------------

df_inventory.tail()
df_inventory.isnull().sum()


inventory_departments = df_inventory['department'].unique()
inventory_departments

df_inventory['drawer_number'].value_counts().sort_index()

#Negative quantity check
inventory_quantity_check = df_inventory[df_inventory['current_quantity'] < 0]
print(f'negative stock quantity: {len(inventory_quantity_check)}')

#Overstocked Items
overstocked_items = df_inventory[df_inventory['current_quantity'] > df_inventory['par_level']]
print(f'Overstocked items: {len(overstocked_items)}')

missing_par_values = df_inventory[df_inventory['par_level'].isnull()]
print(f'missing_par_values: {len(missing_par_values)}')

Duplicated = df_inventory.duplicated(subset=['device_id','drawer_number','medication_id']).sum()
Duplicated

































