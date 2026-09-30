import pandas as pd

df_transactions = pd.read_csv("../data/cleaned/fact_transactions.csv")

df_inventory = pd.read_csv("../data/cleaned/dim_inventory.csv")

df_medications = pd.read_csv("../data/cleaned/dim_medications.csv")

df_devices = pd.read_csv("../data/cleaned/dim_devices.csv")

df_patients = pd.read_csv("../data/cleaned/dim_patients.csv")

df_users = pd.read_csv("../data/cleaned/dim_users.csv")