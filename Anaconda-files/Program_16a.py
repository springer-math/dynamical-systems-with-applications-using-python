# Program 16a: Intersection of implicit curves.
# See Figure 16.10(b).

import numpy as np
import matplotlib.pyplot as plt

A, B = 2.2, 0.15

x, y = np.mgrid[0:4:100j, -4:4:100j]
z1 = A + B*x*np.cos(x**2 + y**2) - B*y*np.sin(x**2 + y**2) - x
z2 = B*x*np.sin(x**2 + y**2) + B*y*np.cos(x**2 + y**2) - y

fig, ax = plt.subplots()
plt.contour(x, y, z1, levels=[0])
plt.contour(x, y, z2, levels=[0], colors='r')
ax.set_xlabel('x(t)', fontsize=15)
ax.set_ylabel('y(t)', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
