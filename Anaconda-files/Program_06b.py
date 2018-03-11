# Program 06b: Surface plot of Hamiltonian. See Figure 6.2(b).
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fun(x, y):
    return y**2 / 2 - 5*np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-10.0, 10.0, 0.1)
y = np.arange(-4.0, 4.0, 0.1)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel(r'$\theta$', fontsize=12)
ax.set_ylabel(r'$\phi$', fontsize=12)
ax.set_zlabel(r'$H(\theta,\phi)$', fontsize=12)
plt.tick_params(labelsize=12)
ax.view_init(30, -70)

plt.show()
