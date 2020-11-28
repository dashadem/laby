import pandas as pd
import matplotlib.pyplot as plt

fx = pd.read_excel('students_info.xlsx')
fx.rename(columns = {'login':'User'}, inplace=True)
fh = pd.read_html('results_ejudge.html')[0]
df = pd.merge(fx, fh)
#задание1
df1 = df.groupby(['group_faculty']).mean()
ax1 = df1.plot(kind='bar', y='Solved')
plt.ylim([0,8])

df2 = df.groupby(['group_out']).mean()
ax2 = df2.plot(kind='bar', y='Solved')
plt.ylim([0,8])

#задание2
f = df[(df['G'] > 9) | (df['H'] > 9)]
print(f[['group_faculty', 'group_out']])

plt.show()