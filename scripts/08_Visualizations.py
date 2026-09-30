import pandas as pd

import matplotlib.pyplot as plt

full_transactions = pd.read_csv("../data/Engineered/full_transactions.csv")

# Bar Chart - Transaction volume by Type 

tx_counts = full_transactions.groupby('transaction_type')['transaction_id'].count()
tx_counts.plot.bar(color='steelblue')
plt.title('Transaction Volume By Type')

# Line Chart - Montly transaction trend

tx_trend = full_transactions.groupby('mon')

