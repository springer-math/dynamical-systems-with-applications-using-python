# Programs 21d: Animation of a JJ limit cycle bifurcation. 
# See Figure 21.9.
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint
fig=plt.figure()
myimages=[]

BJ=1.2;Tmax=100;
def JJ_ODE(x, t):
    return [x[1],kappa-BJ*x[1]-np.sin(x[0])]

time = np.arange(0, Tmax, 0.1) 
x0=[0.1,0.1]
for kappa in np.arange(0.1, 2, 0.1):
    xs = odeint(JJ_ODE, x0, time)
    imgplot = plt.plot(np.sin(xs[:,0]), xs[:,1], "r-")
    myimages.append(imgplot)

my_anim=animation.ArtistAnimation(fig,myimages,interval=100,\
                                  blit=False,repeat_delay=100)
plt.show()