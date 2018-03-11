# Program 21d: Animation of a JJ limit cycle bifurcation.
# See Figure 21.9.

from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np
from scipy.integrate import odeint

fig = plt.figure()
myimages = []

bj = 1.2
tmax = 100

def jj_ode(x, t):
    return [x[1], kappa - bj*x[1] - np.sin(x[0])]

time = np.arange(0, tmax, 0.1)
x0 = [0.1, 0.1]
for kappa in np.arange(0.1, 2, 0.1):
    xs = odeint(jj_ode, x0, time)
    imgplot = plt.plot(np.sin(xs[:, 0]), xs[:, 1], 'r-')
    myimages.append(imgplot)

my_anim = ArtistAnimation(fig, myimages, interval=100, blit=False, repeat_delay=100)
plt.show()
