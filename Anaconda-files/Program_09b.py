# Program 09b: Hamiltonian with two degrees of freedom.
# See Figure 9.5(e).

import numpy as np
from scipy.integrate import odeint
from sympy import sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Maximum time point and total number of time points
tmax, n = 100, 20000
w1 = sqrt(2)
w2 = 1

def hamiltonian_4d(X, t):
    p1, p2, q1, q2 = X
    dp1 = -w1 * q1
    dp2 = -w2 * q2
    dq1 = w1 * p1
    dq2 = w2 * p2
    return (dp1, dp2, dq1, dq2)

t = np.linspace(0, tmax, n)
f = odeint(hamiltonian_4d, (0.5, 1.5, 0.5, 0), t)
p1, p2, q1, q2 = f.T

fig=plt.figure()
ax = Axes3D(fig)

ax.plot(p1, q1, q2, 'b-', lw=0.5)
ax.set_xlabel(r'$p_1$', fontsize=15)
ax.set_ylabel(r'$q_1$', fontsize=15)
ax.set_zlabel(r'$q_2$', fontsize=15)
plt.tick_params(labelsize=12)
ax.set_title('H=1.365416000', fontsize=15)
plt.show()
