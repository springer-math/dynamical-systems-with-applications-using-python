# Program 08c: The Belousov-Zhabotinski Reaction. See Figure 8.16.
# Plotting time series for a 3-dimensional ODE.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# B_Z parameters and initial conditions.
q, f, eps, delta = 3.1746e-5, 1, 0.0099, 2.4802e-5
x0, y0, z0 = 0, 0, 0.1

# Maximum time point and total number of time points.
tmax, n = 50, 10000

def bz_reaction(X, t, q, f, eps, delta):
    x, y, z = X
    dx = (q*y - x*y + x*(1-x)) / eps
    dy = (-q*y - x*y + f*z) / delta
    dz = x-z
    return (dx, dy, dz)

t = np.linspace(0, tmax, n)
f = odeint(bz_reaction, (x0, y0, z0), t, args=((q, f, eps, delta)))
x, y, z = f.T

# Plot time series.
fig = plt.figure(figsize=(15, 5))
fig.subplots_adjust(wspace=0.5, hspace=0.3)
ax1 = fig.add_subplot(1, 3, 1)
ax1.set_title('Relative concentration bromous acid', fontsize=12)
ax2 = fig.add_subplot(1, 3, 2)
ax2.set_title('Relative concentration bromide ions', fontsize=12)
ax3 = fig.add_subplot(1, 3, 3)
ax3.set_title('Relative concentration cerium ions', fontsize=12)

ax1.plot(t, x, 'b-')
ax2.plot(t, y, 'r-')
ax3.plot(t, z, 'm-')

plt.show()
