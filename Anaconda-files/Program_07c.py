# Program 7c: Animation of a SNIC bifurcation. 
# See Figure 7.12.
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint
fig=plt.figure()
myimages=[]
def SNIC(x, t):
    return [x[0]*(1-x[0]**2-x[1]**2)-x[1]*(1+mu+x[0]),
            x[1]*(1-x[0]**2-x[1]**2)+x[0]*(1+mu+x[0])]

time = np.arange(0, 200, 0.01) 
x0=[0.5,0]
for mu in np.arange(-3, 1, 0.1):
    xs = odeint(SNIC, x0, time)
    imgplot = plt.plot(xs[:,0], xs[:,1], "r-")
    myimages.append(imgplot)

my_anim = animation.ArtistAnimation(fig,myimages,interval=100,blit=False,repeat_delay=100)
plt.show()