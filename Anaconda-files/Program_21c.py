# Program 21c: Josephson junction limit cycle.
# See Figure 21.9.

from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

fig = plt.figure()

bj = 1.2
tmax = 100
kappa = 1.4

def jj_ode(x, t):
    return [x[1], kappa - bj*x[1] - np.sin(x[0])]

time = np.arange(0, tmax, 0.1)
x0=[0.1,0.1]
xs = odeint(jj_ode, x0, time)
imgplot = plt.plot(np.sin(xs[:, 0]), xs[:, 1], 'r-')

plt.xlabel(r'$\sin(\phi)$', fontsize=15)
plt.ylabel(r'$\Omega$', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
