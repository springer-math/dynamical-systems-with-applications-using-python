# Program 09c: Phase portrait and Poincare section of a nonautonomous ODE.
# See Figure 9.11(b).

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

xmin, xmax = -2, 2
ymin, ymax = -2, 2

k = 0.3
omega = 1.25
gamma = 0.5

def dx_dt(x, t):
    return [x[1], x[0] - k*x[1] - x[0]**3 + gamma*np.cos(omega*t)]

# Phase portrait
t = np.linspace(0, 500, 10000)
xs = odeint(dx_dt, [1,0], t)
plt.plot(xs[:, 0], xs[:, 1], 'r-', lw=0.5)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.title('Phase portrait')

# The Poincare section.
fig, ax = plt.subplots(figsize=(6, 6))
t = np.linspace(0, 4000 * (2*np.pi) / omega, 16000000)
xs = odeint(dx_dt, [1, 0], t)

x = [xs[4000*i, 0] for i in range(4000)]
y = [xs[4000*i, 1] for i in range(4000)]

ax.scatter(x, y, color='blue', s=0.1)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
plt.title('The Poincare section')

plt.show()
