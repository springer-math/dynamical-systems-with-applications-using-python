# Program 11a: Animation of a limit cycle for a Lienard system.
# See Figure 11.12.

from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np
from scipy.integrate import odeint

fig = plt.figure()
xmin, xmax = -1.5, 1.5
ymin, ymax = -5, 5

ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))

def Lienard(x, t):
    return [mu*x[1] - mu * (-x[0] + x[0]**3), -x[0]/mu]

time = np.arange(0, 20, 0.1)
x0=[1,0]

myimages=[]
for mu in np.arange(0, 5, 0.1):
    xs = odeint(Lienard, x0, time)
    imgplot = plt.plot(xs[:, 0], xs[:, 1], 'r-')
    myimages.append(imgplot)

my_anim = ArtistAnimation(fig, myimages, interval=100, blit=False, repeat_delay=100)
plt.show()
