# Program 21a: The Hodgkin-Huxley Equations.
# See Figures 21.2 and 21.3.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
C_m = 1.0  # uF/cm^2
g_Na = 120.0  # mS/cm^2
g_K = 36.0
g_L = 0.3
V_Na = 50.0  # mV
V_K = -77.0
V_L = -54.402

# See equations (21.4)
def alpha_m(V): return 0.1 * (V + 40.0) / (1.0 - np.exp(-0.1 * (V + 40.0)))
def beta_m(V):  return 4.0 * np.exp(-0.0556 * (V + 65.0))
def alpha_h(V): return 0.07 * np.exp(-0.05 * (V + 65.0))
def beta_h(V):  return 1.0 / (1.0 + np.exp(-0.1 * (V + 35.0)))
def alpha_n(V): return 0.01 * (V + 55.0) / (1.0 - np.exp(-0.1 * (V + 55.0)))
def beta_n(V):  return 0.125 * np.exp(-0.0125 * (V + 65))

# See equation (21.2)
def I_Na(V,m,h): return g_Na * m**3 * h * (V - V_Na)
def I_K(V, n): return g_K * n**4 * (V - V_K)
def I_L(V): return g_L * (V - V_L)

# Input current
def Input_current(t): return 10 * (t > 100) - 10 * (t > 200) + 25 * (t > 300)

t = np.arange(0.0, 400.0, 0.1)

# Set up the ODEs, see equations (21.3)
def hodgkin_huxley(X, t):
    V, m, h, n = X
    dVdt = (Input_current(t) - I_Na(V, m, h) - I_K(V, n) - I_L(V)) / C_m
    dmdt = alpha_m(V) * (1.0 - m) - beta_m(V) * m
    dhdt = alpha_h(V) * (1.0 - h) - beta_h(V) * h
    dndt = alpha_n(V) * (1.0 - n) - beta_n(V) * n
    return (dVdt, dmdt, dhdt, dndt)

y0 = [-65, 0.05, 0.6, 0.32]
X = odeint(hodgkin_huxley, y0, t)
V = X[:, 0]
m = X[:, 1]
h = X[:, 2]
n = X[:, 3]
ina = I_Na(V, m, h)
ik = I_K(V, n)
il = I_L(V)

plt.subplots_adjust(hspace = 1)
plt.figure(1)

plt.subplot(5, 1, 1)
plt.title('Hodgkin-Huxley Neuron')
plt.plot(t, V, 'b')
plt.ylabel('V (mV)')

plt.subplot(5, 1, 2)
plt.plot(t, m, 'k')
plt.ylabel('m(V)')

plt.subplot(5, 1, 3)
plt.plot(t, h, 'r')
plt.ylim(0, 1)
plt.ylabel('h(V)')

plt.subplot(5, 1, 4)
plt.plot(t, n, 'g')
plt.ylim(0, 1)
plt.ylabel('n(V)')

plt.subplot(5, 1, 5)
plt.plot(t, Input_current(t), 'm')
plt.ylabel('Input current')
plt.xlabel('Time (ms)')
plt.ylim(-1, 31)

plt.show()
