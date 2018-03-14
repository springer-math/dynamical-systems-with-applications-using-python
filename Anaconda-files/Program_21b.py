# Program 21b: The Fitzhugh-Nagumo Half-Adder.
# See Figure 21.6.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Input current
def input_1(t): return 1 * (t > 500) - 1 * (t>1000) + 1 * (t > 1500)
def input_2(t): return 1 * (t > 1000)

# Constants
theta = gamma = epsilon = 0.1
tmax, m, c = 2000, -100, 60

t = np.arange(0.0, 2000.0, 0.1)

def fn_odes(X, t):
    u1, v1, u2, v2, u3, v3, u4, v4 = X
    du1 = -u1 * (u1 - theta) * (u1 - 1) - v1 + input_1(t)
    dv1 = epsilon * (u1 - gamma * v1)
    du2 = -u2 * (u2 - theta) * (u2 - 1) - v2 + input_2(t)
    dv2 = epsilon * (u2 - gamma * v2)
    du3 = -u3 * ((u3 - theta) * (u3 - 1) - v3 + 0.8
          / (1 + np.exp(m*v1 + c)) + 0.8
          / (1 + np.exp(m*v2 + c)) - 1.5
          / (1 + np.exp(m*v4 + c)))
    dv3 = epsilon * (u3 - gamma*v3)
    du4 = (-u4 * (u4 - theta) * (u4 - 1) - v4 + 0.45
          / (1 + np.exp(m*v1 + c)) + 0.45
          / (1 + np.exp(m*v2 + c)))
    dv4 = epsilon * (u4 - gamma * v4)
    return (du1, dv1, du2, dv2, du3, dv3, du4, dv4)

y0 = [0.01, 0.01, 0.01, 0.01, 0, 0, 0, 0]
X = odeint(fn_odes, y0, t, rtol=1e-6)
u1, v1, u2, v2, u3, v3, u4, v4 = X.T  # unpack columns

plt.subplots_adjust(hspace=1)
plt.figure(1)

plt.subplot(4, 1, 1)
plt.title('Fitzhugh-Nagumo Half-Adder')
plt.plot(t, u1, 'b')
plt.ylim(-1, 1.5)
plt.ylabel('I$_1$')

plt.subplot(4, 1, 2)
plt.plot(t, u2, 'b')
plt.ylim(-1, 1.5)
plt.ylabel('I$_2$')

plt.subplot(4, 1, 3)
plt.plot(t, u3, 'g')
plt.ylim(0, 1)
plt.ylim(-1, 1.5)
plt.ylabel('O$_1$')

plt.subplot(4, 1, 4)
plt.plot(t, u4, 'g')
plt.ylim(-1, 1.5)
plt.ylabel('O$_2$')
plt.xlabel('Time')

plt.show()
