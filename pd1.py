import pandas as pd

file = pd.read_csv("transactions.csv", index_col = 0)
print(file.loc[file['STATUS'] == 'OK'].sort_values(by='SUM', ascending = False)[0:3])
print(file.loc[file['CONTRACTOR'] == 'Umbrella, Inc', 'SUM'].sum())