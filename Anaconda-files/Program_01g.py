# Program 01g: Animation of a simple curve.
# Hit the green play button (Run file (F5)).

# Run %matplotlib qt5 in IPython console before animating.

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
plt.xlabel('time')
plt.ylabel('sin($\omega$t)')

def init():
    line.set_data([],[])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2*np.pi * (0.1*x*i))
    line.set_data(x, y)
    return line,

# Note: blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=200, blit=True)

plt.show()
