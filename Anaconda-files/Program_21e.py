# Program 21e: Pinched hysteresis in a memristor.
# See Figure 21.12.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
eta, L, Roff, Ron, p, T, w0 = 1.0, 1.0, 70.0, 1.0, 10.0, 20.0, 0.5

t=np.arange(0.0, 40.0, 0.01)

# Set up the ODEs, see equations (21.3)
def memristor(X, t):
    w = X
    dwdt = ((eta * (1 - (2*w - 1) ** (2*p)) * np.sin(2*np.pi * t/T))
           / (Roff - (Roff - Ron) * w))
    return dwdt

X = odeint(memristor, [w0], t, rtol=1e-12)
w = X[:, 0]

plt.plot(np.sin(2*np.pi * t/T), np.sin(2*np.pi * t/T)
        / (Roff - (Roff - Ron) * X[:, 0]), 'b')
plt.xlabel('voltage', fontsize=15)
plt.ylabel('current', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
