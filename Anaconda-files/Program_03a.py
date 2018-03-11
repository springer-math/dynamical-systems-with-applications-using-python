# Program 03a: Phase portrait of a linear system.
# See Figure 3.8(a).

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

# The 2-dimensional linear system
a, b, c, d = 2, 1, 1, 2

def dx_dt(x, t):
    return [a*x[0] + b*x[1], c*x[0] + d*x[1]]

# Trajectories in forward time
ts = np.linspace(0, 4, 100)
ic = np.linspace(-1, 1, 5)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        plt.plot(xs[:, 0], xs[:, 1], 'r-')

# Trajectories in backward time
ts = np.linspace(0, -4, 100)
ic = np.linspace(-1, 1, 5)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        plt.plot(xs[:, 0], xs[:, 1], 'r-')

# Label the axes and set fontsizes
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(-1, 1)
plt.ylim(-1, 1)

# Plot the vectorfield. See lines 10, 12 for system.
X, Y = np.mgrid[-1:1:10j, -1:1:10j]
u = a*X + b*Y
v = c*X + d*Y
pl.quiver(X, Y, u, v, color='b')
plt.show()
