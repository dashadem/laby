import numpy as np
from sympy import *
from scipy. integrate import odeint
import matplotlib.pyplot as plt


x = symbols('x')
y = Function('y')
Eq = dsolve(Eq(diff(y(x), x), - 2*(y(x))))
print(Eq)

def dydt(y, x):
	return -2*y*x
x = np.linspace(0,10,50)
y0 = sqrt(2)
y = odeint(dydt, y0, x)
y = np.array(y).flatten()
plt.plot( x, y)
#plt.show()

