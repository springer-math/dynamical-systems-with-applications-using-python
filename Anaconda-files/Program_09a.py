# Program 09a: Poincare first return map.
# See Figure 9.2.

import matplotlib.pyplot as plt
from sympy import sqrt
import numpy as np
from scipy.integrate import odeint

xmin, xmax = -1, 1
ymin, ymax = -1, 1

def dx_dt(x, t):
    return [-x[1] - x[0] * sqrt(x[0]**2 + x[1]**2),
            x[0] - x[1] * sqrt(x[0]**2 + x[1]**2)]

# Phase portrait
t = np.linspace(0, 16*np.pi, 10000)
xs = odeint(dx_dt, [1, 0], t)
plt.plot(xs[:, 0], xs[:, 1], 'r-')
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax);

# First eight returns on x-axis.
t = np.linspace(0, 9*2*np.pi, 900000)
xs = odeint(dx_dt, [1, 0], t)

for i in range(9):
    print('r{} = {}'.format(i, xs[100000*i, 0]))

plt.show()
