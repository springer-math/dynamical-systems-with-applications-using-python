# Program 02e: Numerical and truncated series solutions.
# See Figure 2.6.

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def ODE2(X, t):
    x = X[0]
    y = X[1]
    dxdt = y
    dydt = x - t ** 2 * y
    return [dxdt, dydt]

X0 = [1, 0]
t = np.linspace(0, 10, 1000)

sol = odeint(ODE2, X0, t)

x = sol[:, 0]
y = sol[:, 1]

fig, ax = plt.subplots()
ax.plot(t, x, label='Numerical')
ax.plot(t, 1 + t**2 / 2 + t**4 / 24, 'r-', label='Truncated series')
plt.xlabel('t', fontsize=15)
plt.ylabel('x', fontsize=15)
plt.tick_params(labelsize=15)
plt.xlim(0, 4)
plt.ylim(0, 4)

ax.legend(loc='lower center', shadow=True)

plt.show()
