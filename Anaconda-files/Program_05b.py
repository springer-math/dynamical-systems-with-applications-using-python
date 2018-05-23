# Program 05b: Example 7, approximate solutions.
# See Figure 5.9.

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

eps = 0.3

def ODE(x, t):
    return eps*x**2-x

x0 = 2
t = np.linspace(0, 10, 1000)

sol = odeint(ODE, x0, t)
x = np.array(sol).flatten()

plt.plot(t, x, label='x(t)')
plt.plot(t, 2*np.exp(-t), label='O(1)')
plt.plot(t, 2*np.exp(-t) + 4*eps*(np.exp(-t)-np.exp(-2*t)), label='O($\epsilon $)')
plt.plot(t, 2*np.exp(-t)+4*eps*(np.exp(-t)-np.exp(-2*t))+ \
         eps**2*8*(np.exp(-t)-2*np.exp(-2*t)+np.exp(-3*t)), label='O($\epsilon^2$)')

plt.xlabel('t', fontsize = 15)
plt.ylabel('x', fontsize = 15)
plt.tick_params(labelsize = 15)
plt.xlim(0, 8)
plt.ylim(0, 2.1)
plt.legend()

plt.show()
