# Programs 19d: Generalized synchronization.
# See Figure 19.8(a).

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
mu=5.7;sigma=16;b=4;r=45.92;
g=8    # When g=4, there is no synchronization.
Tmax=100;

t=np.arange(0.0, Tmax, 0.1)

def Rossler_Lorenz_ODEs(X,t):
    x1,x2,x3,y1,y2,y3,z1,z2,z3 = X
    dx1 = -(x2+x3)
    dx2 = x1+0.2*x2
    dx3 = 0.2+x3*(x1-mu)
    dy1 = sigma*(y2-y1)-g*(y1-x1)
    dy2 = -y1*y3+r*y1-y2
    dy3 = y1*y2-b*y3
    dz1 = sigma*(z2-z1)-g*(z1-x1)
    dz2 = -z1*z3+r*z1-z2
    dz3 = z1*z2-b*z3
    return dx1,dx2,dx3,dy1,dy2,dy3,dz1,dz2,dz3

X = odeint(Rossler_Lorenz_ODEs,[2,-10,44,30,10,20,31,11,22],t,rtol=1e-6)
x1 = X[:,0];x2 = X[:,1];x3 = X[:,2];
y1 = X[:,3];y2 = X[:,4];y3 = X[:,5];
z1 = X[:,6];z2 = X[:,7];z3 = X[:,8];

plt.figure(1)
# Delete first 500 iterates.
plt.plot(y2[500:len(y2)],z2[500:len(z2)])
plt.xlabel(r'$y_2$',fontsize=15)
plt.ylabel(r'$z_2$',fontsize=15)
plt.show()
