# Program 05a: Limit cycle for Fitzhugh-Nagumo.
# See Figure 5.3.

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

theta = 0.14
omega = 0.112
gamma = 2.54
epsilon = 0.01
xmin = -0.5
xmax = 1.5
ymin = 0
ymax = 0.3

def dx_dt(x, t):
    return [-x[0] * (x[0] - theta) * (x[0] - 1) - x[1] + omega,
            epsilon * (x[0] - gamma * x[1])]

# Trajectories in forward time.
xs = odeint(dx_dt, [0.5, 0.09], np.linspace(0, 100, 1000))
plt.plot(xs[:, 0], xs[:,1], 'r-')

# Label the axes and set fontsizes.
plt.xlabel('u', fontsize=15)
plt.ylabel('v', fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax);
# Plot the isoclines.
x=np.arange(xmin, xmax, 0.01)
plt.plot(x, x/gamma, 'b--', x, -x * (x - theta) * (x - 1) + omega, 'b--')

plt.show()
