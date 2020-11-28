from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

n = int(np.loadtxt('large.txt', max_rows=1))
A = np.loadtxt('large.txt', skiprows=1, max_rows=n)
b = np.loadtxt('large.txt', skiprows=n+1)

x = linalg.solve(A,b)

fig, ax = plt.subplots()
ax.bar(np.arange(0,n),x)
plt.grid()
plt.show()