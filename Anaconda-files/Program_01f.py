# Program 01f: Parametric curve in 3D.
# See Figure 1.17.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1, projection='3d')

t = np.linspace(-10, 10, 1000)
x = np.sin(t)
y = np.cos(t)
z = t
ax.plot(x, y, z)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Parametric Curve')

plt.show()
