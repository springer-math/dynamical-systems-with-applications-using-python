# Program 14b: Bifurcation diagram of the logistic map.
# See Figures 14.15 and 14.16.

import numpy as np
import matplotlib.pyplot as plt

def f(x, r):
    return r * x * (1 - x)

ys = []
rs = np.linspace(0, 4, 2000)
#rs = np.linspace(3.5, 4, 2000) # For Figure 14.16.
for r in rs:
    x = 0.1
    for i in range(500):
        x = f(x, r)
    for i in range(50):
        x = f(x, r)
        ys.append([r, x])

ys = np.array(ys)

plt.plot(ys[:, 0], ys[:, 1], 'r.', markersize=0.05)
plt.xlabel('$\mu$', fontsize=15)
plt.ylabel('x', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
