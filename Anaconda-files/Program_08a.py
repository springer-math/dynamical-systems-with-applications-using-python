# Program 08a: The Rossler chaotic attractor. See Fig. 8.10(a).
# In this case, iteration is used to solve the ODEs.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Rossler(x, y, z, a=0.2, b=0.2, c=6.3):
    x_dot = -y - z
    y_dot = x + a*y
    z_dot = b + x*z - c*z
    return (x_dot, y_dot, z_dot)

dt = 0.01
step_count = 50000

xs = np.empty([step_count + 1])
ys = np.empty([step_count + 1])
zs = np.empty([step_count + 1])

# The initial conditions
xs[0], ys[0], zs[0] = (1.0, 1.0, 1.0)

# Iterate.
for i in range(step_count):
    x_dot, y_dot, z_dot = Rossler(xs[i], ys[i], zs[i])
    xs[i+1] = xs[i] + (x_dot * dt)
    ys[i+1] = ys[i] + (y_dot * dt)
    zs[i+1] = zs[i] + (z_dot * dt)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
ax.set_zlabel('z', fontsize=15)
plt.tick_params(labelsize=15)
ax.set_title('Rossler Attractor', fontsize=15)

plt.show()
