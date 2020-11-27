import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("students.csv", sep = ';', header = None)
file.columns = ['prep', 'group', 'mark']

file2 = file.loc[:, ['prep', 'mark']].groupby(by = ['prep', 'mark']).size().transpose().unstack()
ax2 = file2.plot(kind = 'bar', stacked = True)

file1 = file.loc[:, ['group', 'mark']].groupby(by = ['group', 'mark']).size().transpose().unstack()
ax1 = file1.plot(kind = 'bar', stacked = True)

plt.show()