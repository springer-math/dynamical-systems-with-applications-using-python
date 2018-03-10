# Programs 19c: Synchronization between two Lorenz systems.
# See Figure 19.7(b).

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
sigma=16;b=4;r=45.92;
Tmax=100;

t=np.arange(0.0, Tmax, 0.1)

def Two_Lorenz_ODEs(X,t):
    x1,x2,x3,y2,y3=X
    dx1 = sigma*(x2-x1)
    dx2 = -x1*x3+r*x1-x2
    dx3 = x1*x2-b*x3
    dy2 = -x1*y3+r*x1-y2
    dy3 = x1*y2-b*y3
    return dx1,dx2,dx3,dy2,dy3

X = odeint(Two_Lorenz_ODEs,[15,20,30,10,20],t,rtol=1e-6)
x1 = X[:,0];x2 = X[:,1];x3 = X[:,2];
y2 = X[:,3];y3 = X[:,4];

plt.figure(1)

plt.plot(x3,y3)
plt.xlabel(r'$y_3$',fontsize=15)
plt.ylabel(r'$x_3$',fontsize=15)
plt.show()
