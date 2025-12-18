import pandas as pd
import numpy as np

#micro_emf = pd.read_csv('microwaveEMF.csv')
#print(micro_emf.head())
#print(micro_emf.info())

# DataFrame has 20 rows (points in microwave oven)
# All data is in one column, each row containing all measurements seperated by semicolons.
# Data type is object (strings)

# .csv should be comma seperated so need to read with semicolon seperator
micro_emf_comma = pd.read_csv('microwaveEMF.csv', sep=';', header=None)

# Remove last (empty) column
micro_emf_comma = micro_emf_comma.iloc[:, :-1]

# Set column names manually
micro_emf_comma.columns = ['points in microwave oven', 'power density at 5cm', 'power density at 15cm', 'power density at 30cm']

# Remove extra colum (keep only first 4)
micro_emf_comma = micro_emf_comma.iloc[1:]

# Convert columns to numeric
micro_emf_comma['power density at 5cm'] = pd.to_numeric(micro_emf_comma['power density at 5cm'])
micro_emf_comma['power density at 15cm'] = pd.to_numeric(micro_emf_comma['power density at 15cm'])
micro_emf_comma['power density at 30cm'] = pd.to_numeric(micro_emf_comma['power density at 30cm'])

# Set option to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(micro_emf_comma.head())
print(micro_emf_comma.info())

micro_EMF_mean_STD = micro_emf_comma[['power density at 5cm', 'power density at 15cm', 'power density at 30cm']].agg(['mean', 'std'])

import matplotlib.pyplot as plt

micro_EMF_mean_STD.plot(kind='bar')
plt.show()

