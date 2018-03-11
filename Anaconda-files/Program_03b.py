# Program 03b: Nonlinear system, phase portrait with vector plot.
# See Figure 3.12.

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

# The 2-dimensional nonlinear system.
def dx_dt(x, t):
    return [x[1], x[0] * (1 - x[0]**2) + x[1]]

# Trajectories in forward time.
ts = np.linspace(0, 10, 500)
ic = np.linspace(-3, 3, 6)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        plt.plot(xs[:, 0], xs[:, 1], 'r-')

# Trajectories in backward time.
ts = np.linspace(0, -10, 500)
ic = np.linspace(-3, 3, 6)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        plt.plot(xs[:, 0], xs[:, 1], 'r-')

# Label the axes and set fontsizes.
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Plot the vectorfield.
X, Y = np.mgrid[-3:3:20j, -3:3:20j]
u = X
v = X * (1 - X**2) + Y
pl.quiver(X, Y, u, v, color='b')

plt.show()
