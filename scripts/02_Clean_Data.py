import pandas as pd 
import re

df_transactions= pd.read_csv('../data/raw/fact_transactions.csv')

df_medications = pd.read_csv('../data/raw/dim_medications.csv')

df_devices = pd.read_csv('../data/raw/dim_devices.csv')

df_inventory = pd.read_csv('../data/raw/dim_inventory.csv')

df_patients = pd.read_csv('../data/raw/dim_patients.csv')

df_users = pd.read_csv('../data/raw/dim_users.csv')

#Creating copy of orignal data
df_transactions_clean = df_transactions.copy()
df_medications_clean = df_medications.copy()
df_devices_clean = df_devices.copy()
df_inventory_clean = df_inventory.copy()
df_patients_clean1 = df_patients.copy()
df_users_clean = df_users.copy()

df_transactions_clean.tail()
df_transactions_clean.dtypes

# ==================================Clean Transactions dataframe====================

# Standardization for Transaction_type column

df_transactions_clean['transaction_type'] = df_transactions_clean['transaction_type'].astype(str)
df_transactions_clean['transaction_type'] = df_transactions_clean['transaction_type'].str.strip().str.title()
df_transactions_clean['transaction_type'] = df_transactions_clean['transaction_type'].replace('None', None)

df_transactions_clean['transaction_type'].value_counts()
df_transactions_clean['transaction_type'].dtype

df_transactions_clean['transaction_datetime'] = pd.to_datetime(df_transactions_clean['transaction_datetime'])
df_transactions_clean['transaction_datetime'].dtype

# Removing future Dates
df_transactions_clean = df_transactions_clean[df_transactions_clean['transaction_datetime'] < '2024-06-30']

# Removing negative quantities
df_transactions_clean = df_transactions_clean[df_transactions_clean['quantity'] > 0]

# Removing duplicate Transactions
df_transactions_clean = df_transactions_clean.drop_duplicates(subset='transaction_id', keep= 'first')

# Removing Missing user_Ids
df_transactions_clean['user_id'] = df_transactions_clean['user_id'].fillna('Unknown User')

# Reviewing unknown users
unknown_users = df_transactions_clean[df_transactions_clean['user_id'] == 'Unknown User']
unknown_users



df_transactions_clean[df_transactions_clean['order_number'].isnull()]

df_transactions_clean.isnull().sum()

df_transactions_clean.shape

df_transactions_clean.tail()



# ==================================Clean Medications dataframe====================

df_medications_clean.tail()

# Show rows where medication_class is NULL
df_medications_clean[df_medications_clean['medication_class'].isnull()]

# Filling medication class for NULL values
df_medications_clean.loc[df_medications_clean['medication_id'] == 'MED-043', 'medication_class'] = 3
df_medications_clean.loc[df_medications_clean['medication_id'] == 'MED-049', 'medication_class'] = 4

# Show medication_class with incorrect value
df_medications_clean[df_medications_clean['medication_class'] == 99.0]

# Correcting medication_class with proper value
df_medications_clean.loc[df_medications_clean['medication_id'] == 'MED-050', 'medication_class'] = 3

#Creating Standardization for medication_category
df_medications_clean['medication_category'] = df_medications_clean['medication_category'].str.strip().str.title()

# Removing double spacing between medication_name
df_medications_clean['medication_name'] = df_medications_clean['medication_name'].str.replace('  ','').str.strip()

df_medications_clean['medication_name'] = df_medications_clean['medication_name'].str.title()

df_medications_clean.isnull().sum()


# ==================================Clean Users dataframe======================

df_users_clean[df_users_clean['areas_assigned'].isnull()]

#Filling missing areas
df_users_clean['areas_assigned'] = df_users_clean['areas_assigned'].fillna('Unassigned')

#Standardization for user_role
df_users_clean['user_role'] = df_users_clean['user_role'].str.strip().str.title()

df_users_clean['user_name'].unique()

# Custom function to correct user_name format
def standardize_name(user_name):
    if pd.isnull(user_name):
        return user_name
    
    user_name = user_name.strip()
    
    #Already correct format
    if re.match(r'^[A-Z]\.[A-Za-z]+$',user_name):
        return user_name
    
    # Last, First Format - Smith, J
    if ',' in user_name:
        parts = user_name.split(',')
        last = parts[0].strip().title()
        first = parts[1][0].strip().upper()
        return f"{first}.{last}" 
    
      # Full name — John Smith or Miller L
    parts = user_name.strip().split()
    if len(parts) == 2:
        first = parts[0][0].upper()
        last = parts[1].strip('.').title()
        return f"{first}.{last}"
    
    # Lowercase with dot — d.thomas
    if '.' in user_name:
        parts = user_name.split('.')
        first = parts[0][0].upper()
        last = parts[1].title()
        return f"{first}.{last}"
    
    return user_name  # return as-is if no pattern matches

df_users_clean[df_users_clean['user_name'].isin(['.Williams', 'M.L'])]

df_users_clean['user_name'] = df_users_clean['user_name'].replace({
    '.Williams': 'D.Williams',
    'M.L': 'M.Lopez'
})

# Applying above function to user_role
df_users_clean['user_name'] = df_users_clean['user_name'].apply(standardize_name)
df_users_clean['user_name'].unique()

#Dropping duplicated entry for a user
df_users_clean[df_users_clean['user_name'].duplicated(keep=False)]

#Dropping duplicate users except first occurence
df_users_clean= df_users_clean.drop_duplicates(subset='user_name',keep='first')

df_users_clean.isnull().sum()

df_users_clean[df_users_clean[]]


# ==================================Clean Patients dataframe======================

df_patients_clean1.tail()

df_patients_clean1 = df_patients.copy()

df_patients_clean1['visit_status'] = df_patients_clean1['visit_status'].str.strip()

#Correcting incorrect values in visit_status
status_map = {
    'Adm':'Admitted',
    'Admited': 'Admitted',
    'Dischargd':'Discharged',
    'Transfered':'Transferred',
}

df_patients_clean1['visit_status'] = df_patients_clean1['visit_status'].replace(status_map)

df_patients_clean1['patient_type'] = df_patients_clean1['patient_type'].str.strip().str.title()

df_patients_clean1['visit_status'] = df_patients_clean1['visit_status'].str.strip().str.title()

df_patients_clean1['visit_status'].value_counts()

#Converting 'visit_date' to date_time object
df_patients_clean1['visit_date'] = pd.to_datetime(df_patients_clean1['visit_date'], errors='coerce')

df_patients_clean1['visit_date'].astype

missing_patients_age = df_patients_clean1[df_patients_clean1['age'].isnull()]
missing_patients_age

missing_patients_gender = df_patients_clean1[df_patients_clean1['gender'].isnull()]

#Creating standardisation for gender column
gender_map = {
    'Male':'M',
    'Female':'F',
    'm':'M',
    }

df_patients_clean1['gender'] = df_patients_clean1['gender'].replace(gender_map)
df_patients_clean1['gender'].value_counts()

df_patients_clean1.isnull().sum()


# ==================================Clean Inventory dataframe======================

df_inventory_clean = df_inventory.copy()

# Flag missing medication_class with -1
df_inventory_clean['medication_class'] = df_inventory_clean['medication_class'].fillna(-1)

# Fill missing par_level with median by medication_class
df_inventory_clean['par_level'] = df_inventory_clean.groupby('medication_class')['par_level'].transform(
    lambda x: x.fillna(x.median())
)

# Fix negative quantities
df_inventory_clean['current_quantity'] = df_inventory_clean['current_quantity'].clip(lower=0)

# Remove duplicates
df_inventory_clean = df_inventory_clean.drop_duplicates(
    subset=['device_id','drawer_number','medication_id'], keep='first'
)

# Create needs_restock flag
df_inventory_clean['needs_restock'] = (
    df_inventory_clean['current_quantity'] < df_inventory_clean['par_level'] * 0.25
).astype(int)

# Verify
print(f"Rows: {len(df_inventory_clean)}")
print(df_inventory_clean['needs_restock'].value_counts())

# Exporting  all clean dataframes into cleaned data folder

df_transactions_cleaned = df_transactions_clean.to_csv('../data/cleaned/fact_transactions.csv', index=False)

df_medications_cleaned = df_medications_clean.to_csv('../data/cleaned/dim_medications.csv', index=False)

df_users_cleaned = df_users_clean.to_csv('../data/cleaned/dim_users.csv', index=False)

df_patients_cleaned = df_patients_clean1.to_csv('../data/cleaned/dim_patients.csv', index=False)

df_inventory_cleaned = df_inventory_clean.to_csv('../data/cleaned/dim_inventory.csv', index=False)

df_devices_cleaned = df_devices_clean.to_csv('../data/cleaned/dim_devices.csv', index= False)















































    
    
    










 











