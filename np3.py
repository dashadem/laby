import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

y = [float(i) for i in open('start.dat.txt', 'r')]
e = np.eye(len(y))
i = -1*np.eye(len(y)-1)
a = np.zeros(len(y)-1)
b = np.zeros((len(y), 1))
A = np.vstack([a,i])
A = np.column_stack([A, b])
A = A + e
fig, ax = plt.subplots()
ax.plot(y)
X = len(y)
Y = max(y)

def animate(i):
    global y
    y = y - 0.5 * np.dot(A, y)
    ax.clear()
    ax.plot(y)
    ax.set_ylim(0, Y)
    ax.set_xlim(0, X)
    ax.grid(True)


ani = animation.FuncAnimation(fig, animate, frames=255, interval=20)
ani.save('anim.gif',
         writer='pillow',
         fps=30)