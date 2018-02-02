# Hopf Bifurcation
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint

fig=plt.figure()
myimages=[]

def Hopf(x, t):
    return [x[1]+mu*x[0]-x[0]*x[1]**2, mu*x[1]-x[0]-x[1]**3]

time = np.arange(0, 200, 0.01)
x0=[1,0]
for mu in np.arange(-1, 1, 0.1):
    xs = odeint(Hopf, x0, time)
    imgplot = plt.plot(xs[:,0], xs[:,1], "r-")
    myimages.append(imgplot)
   
my_anim = animation.ArtistAnimation(fig,myimages,interval=100,blit=False,repeat_delay=100)
plt.show()