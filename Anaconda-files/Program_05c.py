 # Program 05c: Error between xN and x0. See Figure 5.10.
# Error between one term solution and numerical solution.

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def dx_dt(x, t):
    return [x[1], 0.01 * x[0] ** 3 - x[0]]

x0 = [1, 0]
ts = np.linspace(0, 100, 2000)
xs = odeint(dx_dt, x0, ts)
xN = xs[:, 0]

xpert0 = np.cos(ts)
plt.plot(ts, xN - xpert0)
plt.xlabel('t')
plt.ylabel('$x_N-x_0$')

plt.show()
