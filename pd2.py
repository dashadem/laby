import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("flights.csv", index_col = 0)
f = file.groupby('CARGO').sum()
f1 = file[file['CARGO'] =='Nimble'].count()[0]
f2 = file[file['CARGO'] =='Medium'].count()[0]
f3 = file[file['CARGO'] =='Jumbo'].count()[0]
f.loc[0:3, 'NUMBER'] = f1, f2, f3

ax1 = f.PRICE.plot(kind = 'bar')
ax2 = f.WEIGHT.plot(kind = 'bar')
ax3 = f.NUMBER.plot(kind = 'bar')
plt.show()