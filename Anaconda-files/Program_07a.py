# Program 07a: Animation of a simple curve. Saddle-node bifurcation.
# See Figure 7.2.
# Animation of mu-x**2, as mu increases from mu=-3 to mu=3.
# Type - %matplotlib qt5 - in Console window.

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

xmin, xmax = -4, 4
mu_min, mu_max = -3, 3

# Set up the figure.
fig = plt.figure()

ax = plt.axes(xlim=(xmin, xmax), ylim=(xmin, xmax))
line, = ax.plot([], [], lw=2)
ax.plot([xmin, xmax], [0,0], 'm')
ax.plot([0, 0], [xmin, xmax], 'm')

def init():
    line.set_data([], [])
    return line,

# Animate mu-x^**2, where -3<mu<3.
def animate(mu):
    x = np.linspace(xmin, xmax, 100)
    y = mu - x**2
    line.set_data(x, y)
    return line,

bifurcation = FuncAnimation(fig, animate, init_func=init,
                            frames=np.linspace(mu_min, mu_max, 1000),
                            interval=10, blit=True)

plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)

plt.show()
